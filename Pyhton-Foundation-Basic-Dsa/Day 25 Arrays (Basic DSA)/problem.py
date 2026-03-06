# Find the maximum number in a list

numbers=[10,5,30,15]

max_num=numbers[0]

for n in numbers:
    if n>max_num:
        max_num=n

print("Maximum:",max_num)


# Linear Search

numbers=[10,20,30,40,50]

target=int(input("Enter number:"))

found=False

for n in numbers:
    if n==target:
        found=True
        break

if found:
    print("Number Found")
else:
    print("Number Not Found")


#Take 5 numbers input from user, make a list and print sum, maximum and minimum

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)

print("List:", numbers)
print("Sum:", total)
print("Maximum:", maximum)
print("Minimum:", minimum)