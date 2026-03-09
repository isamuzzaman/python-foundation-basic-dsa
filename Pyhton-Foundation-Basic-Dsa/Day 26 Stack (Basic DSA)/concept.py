#1)
stack=[]

stack.append(10)   # push
stack.append(20)
stack.append(30)

print(stack)

stack.pop()        # pop
print(stack)

# Task 1 (Easy)

#Push 5 numbers in stack then pop 2

stack=[]

for i in range(5):
    num=int(input("Enter number :"))
    stack.append(num)

print("Stack :",stack)

stack.pop()
stack.pop()

print("After pop :",stack)

# Task 2 (Medium)

#Checking if a stack is empty or not

stack=[]

if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
