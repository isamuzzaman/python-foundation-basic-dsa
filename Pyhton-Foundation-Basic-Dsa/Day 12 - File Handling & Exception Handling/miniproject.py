# Student file manager
with open("students.txt","a") as file:
    name=input("Enter student name :")
    cgpa=input("Enter cgpa :")
    file.write(f"{name}-{cgpa}")
with open("students.txt","r") as file:
    print("Student Records :")
    print(file.read())    