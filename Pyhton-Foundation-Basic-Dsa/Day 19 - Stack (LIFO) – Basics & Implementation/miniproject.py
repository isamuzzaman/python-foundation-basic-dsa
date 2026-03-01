# Undo system simulator
stack = []

while True:
    print("1. Do Action")
    print("2. Undo")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        action = input("Enter action: ")
        stack.append(action)
        print("Action saved")

    elif choice == "2":
        if stack:
            print("Undo:", stack.pop())
        else:
            print("Nothing to undo")

    elif choice == "3":
        break