def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Infinty"
    else:
        return a/b
print("Add :",sum(2,4))
print("Subtract :",sub(2,4))
print("Multiplication :",multi(2,4))
print("Divide :",div(2,4))