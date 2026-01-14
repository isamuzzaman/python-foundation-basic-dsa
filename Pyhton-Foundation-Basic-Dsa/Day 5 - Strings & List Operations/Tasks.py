# Common String Methods
text = "python programming"

print(text.upper())
print(len(text))
print(text.lower())
print(text.title())
print(text.count("p"))
print(text.replace("python", "Java"))

# List method finding max & min
numbers=[]
for i in range(3):
    numbers.append(int(input("Enter a number :")))
print("Max Number :",max(numbers))
print("Min Numbers :",min(numbers))    
