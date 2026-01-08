
n=int(input("Enter number :"))
if n%2==0:
    print("Even")
else:
    print("Odd")    

if n>0:
    print("Possitive")
elif n<0:
    print("Negative")
else:
    print("Zero")


for i in range(1,11):
    table=n*i
    print(f"{n}x{i}={table}")                   