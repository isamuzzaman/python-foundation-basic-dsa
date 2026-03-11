#1)
queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue
queue.pop(0)

print("After Dequeue:", queue)

#2)
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

queue.popleft()

print(queue)

#Given a queue, reverse the first k elements and keep the rest in the same order

def reverse_k(queue, k):
    stack = []
    
    # Step 1
    for i in range(k):
        stack.append(queue.pop(0))
    
    # Step 2
    while stack:
        queue.append(stack.pop())
    
    # Step 3
    for i in range(len(queue) - k):
        queue.append(queue.pop(0))
    
    return queue


q = [1, 2, 3, 4, 5]
print(reverse_k(q, 3))