# Take number and return square
def functions():
    n=int(input("Enter a number :"))
    return n*n
result=functions()
print("The result is :",result)

# Take a list and return sum max and min
def function(numbers):
    total=sum(numbers)
    maximum=max(numbers)
    minimum=min(numbers)
    return total,maximum,minimum
num=[10,20,30,40,50]
s,mx,mn=function(num) 
print("Sum:",s)
print("Max:",mx)
print("Min:",mn)
