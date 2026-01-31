# Debugging with print()
def divide(a, b):
    print("a =", a, "b =", b)
    return a / b

print(divide(10, 2))
# Docstrings
def add(a, b):
    """
    Returns the sum of two numbers
    """
    return a + b

print(add.__doc__)

# Clean & Optimized Code
def add(x, y):
    return x + y

print(add(10, 20))
