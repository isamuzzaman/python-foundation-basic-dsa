# Stack Based Menu System
stack=[]

while True:
    print("1.Push")
    print("2.Pop")
    print("3.Show Stack")
    print("4.Exit")

    choice=input("Enter choice :")

    if choice=="1":
        num=int(input("Enter number :"))
        stack.append(num)

    elif choice=="2":
        if not stack:
            print("Stack empty")
        else:
            print("Removed :",stack.pop())

    elif choice=="3":
        print("Stack :",stack)

    elif choice=="4":
        break

    else:
        print("Invalid choice")