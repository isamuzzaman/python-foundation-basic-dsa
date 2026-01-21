# Task 1: person class->name,age
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
s1=person("Isam",21)
s1.display()

# Task 2: student class->name,dept,cgpa        
class student:
    def __init__(self,name,dept,cgpa):
        self.name=name
        self.dept=dept
        self.cgpa=cgpa
    def info(self):
        print("Name :",self.name)
        print("Department :",self.dept)
        print("CGPA :",self.cgpa)
s1=student("Isam","Swe",3.91)
s1.info()            

        