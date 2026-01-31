# Error-Safe Calculator
def divide(a,b):
    """Safely divide two numbers"""
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by Zero"
print(divide(10,4))