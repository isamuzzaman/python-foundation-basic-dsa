# Student class (Grade calculator)
class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def grade(self):
        if self.cgpa>=3.75:
            return "A"   
        elif self.cgpa>=3.50:
            return "A-"
        else:
            return "B" 
students=[]
students.append(Student("Isam",3.81))
students.append(Student("Rana",3.80))
for s in students:
    print(s.name,s.grade())       

# Multiple student object->List->Student info print
class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def info(self):
        print("Name :",self.name)
        print("Cgpa :",self.cgpa)
        print("Grade :",self.grade())    
    def grade(self):
        if self.cgpa>=3.75:
            return "A"
        else:
            return "-A"
students=[]
students.append(Student("Rahim",3.75))
students.append(Student("Karim",3.77))
for s in students:
   s.info()

        


      