import tkinter as tk
import os
import socket

def get_username():
    return os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown'

def get_hostname():
    try:
        return socket.gethostname()
    except:
        return 'localhost'

def expand_variables(text):
    import re
    def replace_var(match):
        var_name = match.group(1)
        return os.environ.get(var_name, match.group(0))
    return re.sub(r'\$(\w+)', replace_var, text)

username = get_username()
hostname = get_hostname()
window_title = f"Эмулятор - [{username}@{hostname}]"

def run_command():
    data = entry.get().strip()
    if not data:
        return
    expanded_data = expand_variables(data)
    parts = expanded_data.split()
    command = parts[0]
    args = parts[1:]
    if command == 'exit':
        root.destroy()
        return
    elif command == 'ls':
        output_text.insert(tk.END, f"{command} {' '.join(args)}\n")
    elif command == 'cd':
        output_text.insert(tk.END, f"{command} {' '.join(args)}\n")
    else:
        output_text.insert(tk.END, f"{command} : command is not found\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title(window_title)
root.configure(bg='black')

output_text = tk.Text(root, height=20, width=60, bg='black', fg='white', insertbackground='white')
output_text.pack(fill=tk.BOTH, expand=True)

entry_frame = tk.Frame(root, bg='black')
entry_frame.pack(fill=tk.X)

prompt_label = tk.Label(entry_frame, text=f"{username}@{hostname}: ~$ ", bg='black', fg='white')
prompt_label.pack(side=tk.LEFT)

entry = tk.Entry(entry_frame, width=50, bg='black', fg='white', insertbackground='white', relief=tk.FLAT)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

def on_enter(event):
    run_command()

entry.bind('<Return>', on_enter)

root.mainloop()