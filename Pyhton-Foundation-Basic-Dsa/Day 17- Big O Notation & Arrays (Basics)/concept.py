# O(1) → constant time

# O(n) → linear time

# O(n²) → nested loop

# O(1)
print("Hello")

# O(n)
for i in range(2):
    print(i)

# O(n^2)
for i in range(2):
    for j in range(2):
        print(i, j)

# Array Concept (Using List in Python)



arr = [10, 20, 30, 40]
print(arr[0])     # Access
arr.append(50)    # Insert

# Traversing an Array
for x in arr:
    print(x)

# Searching in Array (Linear Search)
arr = [5, 8, 2, 9]
key = 2
found = False

for x in arr:
    if x == key:
        found = True
        break

print("Found" if found else "Not Found")


       