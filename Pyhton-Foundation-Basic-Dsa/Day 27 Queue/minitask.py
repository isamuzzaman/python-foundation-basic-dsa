#Simulate a Bank Queue (or Customer Service Queue) using a program.
queue = []

while True:
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Show Queue")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Customer Name: ")
        queue.append(name)
        print(name, "added to queue")

    elif choice == "2":
        if queue:
            served = queue.pop(0)
            print(served, "served")
        else:
            print("No customers")

    elif choice == "3":
        print("Current Queue:", queue)

    elif choice == "4":
        print("System Closed")
        break

    else:
        print("Invalid choice")