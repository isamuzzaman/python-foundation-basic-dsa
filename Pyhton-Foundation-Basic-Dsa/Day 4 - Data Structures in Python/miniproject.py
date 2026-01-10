# Student Record Manager

students=[]
n=int(input("Enter numbers :"))
for i in range(n):
    name=input("Enter name :")
    age=int(input("Enter age :"))
    dept=input("Enter dept :")

    student={
      "name":name,
      "age":age,
      "dept":dept
    }    
    students.append(student)
print(".......Student Records........")    
for student in students:
    print("Name :",student["name"])
    print("Age :",student["age"])
    print("Dept :",student["dept"])
    print("....................")