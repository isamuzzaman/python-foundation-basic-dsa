# Student Management System
class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa

    def grade(self):
        if self.cgpa >= 3.75:
            return "A"
        elif self.cgpa >= 3.50:
            return "A-"
        else:
            return "B"  
          
    def info(self):
        print("Name :",self.name)
        print("Cgpa :",self.cgpa)
        print("Grade :",self.grade())

students=[]
while True:
     print("1. Add Student")
     print("2. Show All Students")
     print("3. Exit")
     choice=input("Enter your choice :")
     if choice=="1":
         name=input("Enter your name :")
         cgpa=float(input("Enter your cgpa:"))
         s=Student(name,cgpa)
         students.append(s)
     elif choice=="2":
         if not students:
             print("Not student")
         else:
             for s in students:
                 s.info()
     elif choice == "3":
        print("Program closed")
        break

     else:
        print("Invalid choice")            
         
         
                   




        