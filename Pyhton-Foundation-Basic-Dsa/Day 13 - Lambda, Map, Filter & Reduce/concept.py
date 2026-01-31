# Lambda function
square = lambda x: x * x
print(square(5))
# map()
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, numbers))
print(squares)
# filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
# reduce()
from functools import reduce

total = reduce(lambda a, b: a + b, numbers)
print(total)
