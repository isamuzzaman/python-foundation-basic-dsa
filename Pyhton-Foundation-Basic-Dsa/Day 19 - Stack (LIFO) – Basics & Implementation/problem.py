# Reverse a string using stack
stack=[]
s=input("Enter a word :")
rev=""
for ch in s:
    stack.append(ch)
while stack:
    rev=rev+stack.pop()    
print("The reverse of the word is :",rev)    
