# Set
name={1,2,4,3,3,4,5}
print(name)

a = {1, 2, 3}
b = {3, 4, 5}
print(a|b) #union
print(a & b) #intersection
print(a-b) #difference

# Tuple

data=("isam",33,"Swe")
name,age,dept=data
print(name,age,dept)

# Break
for i in range(1,6):
    if i==3:
        break
    print(i)

#Continue
for i in range(1,6):
    if i==3:
        continue
    print(i)
#Pass
for i in range(1,6):
    if i==3:
        pass
    print(i)