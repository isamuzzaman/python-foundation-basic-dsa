# Student Record Manager (Dictionary Version)
students = {}

while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Name: ")
        cgpa = float(input("CGPA: "))
        students[name] = {"cgpa": cgpa}
    
    elif choice == "2":
        for name, info in students.items():
            print("Name:", name, "CGPA:", info[cgpa])
    
    elif choice == "3":
        print("Program closed")
        break
    
    else:
        print("Invalid choice")
