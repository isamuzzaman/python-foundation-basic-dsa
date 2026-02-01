# Dictionary Basics
student = {"name": "Isam", "age": 22, "dept": "SWE"}
print(student["name"])
print(student.get("cgpa", "Not Found"))
# Nested dictionary
students = {
    "s1": {"name": "Isam", "cgpa": 3.91},
    "s2": {"name": "Rana", "cgpa": 3.75}
}
for key, val in students.items():
    print(key, "-", val["name"], val["cgpa"])
# Nested Lists + Dictionary
data = [
    {"name": "Isam", "marks": [90, 85, 88]},
    {"name": "Rana", "marks": [75, 80, 78]}
]

for student in data:
    print(student["name"], "Total Marks:", sum(student["marks"]))
