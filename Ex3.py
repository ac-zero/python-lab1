i = 0
task = []
exit_status = 0
while exit_status == 0:
    print("To-do Manager:")
    print("1. Insert new task")
    print("2. Remove task")
    print("3. Show all tasks")
    print("4. Exit")

    choice = int(input())

    if choice == 1 :
        print("Insert name: ")
        name = input()
        task.append(name)
        i += 1
        print(i)
    elif choice == 2 :
        print("Insert name: ")
        name = input()
        task.remove(name)
        i -= 1
    elif choice == 3 :
        for x in range(1,i+1):
            print(str(x) + ". " + task[x-1])
    elif choice == 4:
        exit_status = 1
    else:
        print("Wrong number!")
