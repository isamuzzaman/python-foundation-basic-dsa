# Simple Queue using List
queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue
queue.pop(0)

# Peek
print(queue[0])


# Queue Class
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0
    

    
# Better Way (Optimization)

from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.popleft()