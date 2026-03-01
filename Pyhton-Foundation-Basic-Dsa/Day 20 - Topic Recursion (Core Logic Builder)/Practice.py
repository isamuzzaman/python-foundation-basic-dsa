# Practice Problems (Recursion)
# Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
# Fibonacci
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
# Sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
# Reverse a string
def reverse_string(s):
    if s == "":
        return ""
    return s[-1] + reverse_string(s[:-1])
# Check palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])