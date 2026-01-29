# Write to a file
file = open("data.txt", "w")
file.write("Hello Python\n")
file.write("File handling practice")
file.close()
# Read from a file
file = open("data.txt", "r")
print(file.read())
file.close()
# Append to a file
file = open("data.txt", "a")
file.write("\nNew line added")
file.close()
# Using with Statement
with open("data.txt", "r") as file:
    print(file.read())
# Exception handeling
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
