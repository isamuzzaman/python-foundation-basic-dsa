# For Loop:

n=int(input("Enter number N:"))
sum_even=0
for i in range(1,n+1):
    if i%2==0:
        sum_even=sum_even+i
print("Sum of even numbers :",sum_even)        

# While loop:
n=int(input("Enter number N:"))
sum_even=0
i=1
while i<n:
    if i%2==0:
      sum_even=sum_even+i

    i=i+1

print("Sum of even numbers :",sum_even)
