# Unique Student Registration System
students = set()

while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        name = input("Enter student name : ")
        students.add(name)

    elif choice == "2":
        print("Registered Students:")
        for s in students:
            print("-", s)

    elif choice == "3":
        print("Program closed")
        break

    else:
        print("Invalid choice")
       
                            
