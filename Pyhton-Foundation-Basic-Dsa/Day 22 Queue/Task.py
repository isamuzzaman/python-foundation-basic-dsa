# Generate Binary Numbers from 1 to N using Queue

from collections import deque
def generate_binary_number(n):
    q=deque()
    q.append("1")
    for i in range(n):
        current=q.popleft()
        print(current,end=" ")
        q.append(current+"0")
        q.append(current+"1")



