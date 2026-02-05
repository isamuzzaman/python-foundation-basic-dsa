# Find the sum of array elements
arr = [10, 23, 42, 13]
total = 0

for x in arr:
    total = total + x

print(total)

# Find max & min from an array without using built-in functions
arr = [11, 12, 13, 14, 15]

max_val = arr[0]
min_val = arr[0]

for x in arr:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

print("Maximum:", max_val)
print("Minimum:", min_val)
