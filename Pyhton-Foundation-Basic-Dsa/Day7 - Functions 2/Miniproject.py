# Menu-driven calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5. Exit")
    choice=(input("Enter your choice :"))
    if choice=="5":
        print("Calculator closed")
        break
    if choice in["1","2","3","4"]:
        x=int(input("Enter your number :"))
        y=int(input("Enter your number :"))
        if choice=="1":
            print("Add :",add(x,y))
        elif choice=="2":
            print("Sub :",subtract(x,y))    
        elif choice=="3":
            print("Multiply:",multiply(x,y))
        elif choice=="4":
            print("Divide:",divide(x,y))    
    else:
        print("Invalid choice")      