for i in range(int(input())):
    command = input()
    if command.startswith('Simon says '):
        print(command[11:])
