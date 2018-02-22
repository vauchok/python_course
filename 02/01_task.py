# 01_task.py

while True:
    try:
        n = int(input("Input n: "))
    except ValueError:
        print("You inputted wrong value")
    else:
        break

initialized_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    try:

        # Initializing list of commands
        commands = []
        for i in range(0, n):
            commands.append(input())

        # Doing some command from initialized list  of commands
        for i in range(0, n):
            pattern = commands[i].split()
            if pattern[0] == 'insert':
                initialized_list.insert(int(pattern[1]), int(pattern[2]))
            elif pattern[0] == 'print':
                print(initialized_list)
            elif pattern[0] == 'remove':
                initialized_list.remove(int(pattern[1]))
            elif pattern[0] == 'append':
                initialized_list.append(int(pattern[1]))
            elif pattern[0] == 'sort':
                initialized_list.sort()
            elif pattern[0] == 'pop':
                initialized_list.pop(-1)
            elif pattern[0] == 'reverse':
                initialized_list.reverse()
            else:
                raise Exception("Some command doesn't exist, please input again:")
    except (Exception, IndexError, ValueError) as e:
        print(e)
    else:
break
