while True:
    data = input('username@hostname: ~$ ')
    command, *args = data.split()

    if command == 'exit':
        break
    elif command == 'ls':
        print (command, args)
    elif command == 'cd':
        print (command, args)
    else:
        print(f'{command} : command is not found') 
