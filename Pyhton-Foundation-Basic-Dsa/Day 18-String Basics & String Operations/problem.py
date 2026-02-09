# Problem 1: Count number of vowels in a string
s=input("Enter a single string :")
count=0
for ch in s:
    if ch in "aeiouAEIOU":
        count=count+1
print("Number of vowels :",count)        

# Problem 2: Check whether a string is palindrome
s=input("Enter a string :")
rev=""
for ch in s:
    rev=ch+rev
if s==rev:
    print("Palindrome")
else:
    print("Not palindrome")