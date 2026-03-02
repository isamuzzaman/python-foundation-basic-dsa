# Stack using Python List
stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

# Pop
stack.pop()

# Peek (top element)
print(stack[-1])


# Build Stack Class

class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty" 
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"    
    def is_empty(self):
        return len(self.items)==0

