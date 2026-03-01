# Stack Implementation (Using List)
stack = []

# push
stack.append(10)
stack.append(20)

# pop
print(stack.pop())

# peek
print(stack[-1])

# is empty
print(len(stack) == 0)

# Stack Traversal
for item in stack:
    print(item)