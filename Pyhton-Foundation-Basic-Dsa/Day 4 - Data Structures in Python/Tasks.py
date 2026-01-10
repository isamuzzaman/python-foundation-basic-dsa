# Task1:Print 2nd name from dictionary

names={
    "name1":"Isam",
    "name2":"Rana",
    "name3":"Jony",
    "name4":"Bunty",
    "name5":"Aunty"
}
print(names["name2"])

# Task2:Make a dictionary and print key and values using loops

student={
    "name":"Isam",
    "age":22,
    "dept":"Swe"
}
for key,value in student.items():
    print(key,":",value)
