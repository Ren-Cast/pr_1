import tkinter as tk # Импорт библиотеки для создания графического интерфейса
import os # Импорт модуля для работы с операционной системой
import socket # Импорт модуля для работы с сетевыми функциями


# Функция для получения имени пользователя
def get_username():
    return os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown'

def get_hostname():
    try:
        return socket.gethostname()
    except:
        return 'localhost'

def expand_variables(text):     # раскрывает переменные окружения в тексте
    import re    # импорт модуля для работы с регулярными выражениями
    def replace_var(match):     # вспомогательная функция для замены переменных
        var_name = match.group(1)
        return os.environ.get(var_name, match.group(0))
    return re.sub(r'\$(\w+)', replace_var, text)

username = get_username()
hostname = get_hostname()
window_title = "VFS"

def run_command():
    data = entry.get().strip()
    if not data:
        return
    
    # Расширение переменных окружения
    expanded_data = expand_variables(data)

    # Простой парсер: разделение ввода на команду и аргументы по пробелам
    parts = expanded_data.split()
    command = parts[0]
    args = parts[1:]

    # Обработка команд
    if command == 'exit':
        root.destroy()
        return
    elif command == 'ls':
        # Команда-заглушка, выводящая свое имя и аргументы
        output_text.insert(tk.END, f"{command} {' '.join(args)}\n")
    elif command == 'cd':
        # Команда-заглушка, выводящая свое имя и аргументы
        output_text.insert(tk.END, f"{command} {' '.join(args)}\n")
    else:
        # Обработка неизвестных команд (ошибка)
        output_text.insert(tk.END, f"{command} : command is not found\n")

    # Очистка поля ввода
    entry.delete(0, tk.END)

# Создание главного окна GUI
root = tk.Tk()
root.title(window_title)
root.configure(bg='black')

# Текстовое поле для вывода результатов
output_text = tk.Text(root, height=20, width=60, bg='black', fg='white', insertbackground='white')
output_text.pack(fill=tk.BOTH, expand=True)

# Фрейм для поля ввода и приглашения
entry_frame = tk.Frame(root, bg='black')
entry_frame.pack(fill=tk.X)

# Метка с приглашением к вводу
prompt_label = tk.Label(entry_frame, text=f"{username}@{hostname}: ~$ ", bg='black', fg='white')
prompt_label.pack(side=tk.LEFT)

# Поле ввода команд
entry = tk.Entry(entry_frame, width=50, bg='black', fg='white', insertbackground='white', relief=tk.FLAT)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Обработчик нажатия Enter
def on_enter(event):
    run_command()

entry.bind('<Return>', on_enter)


# Запуск главного цикла GUI
root.mainloop()