# Student CGPA Processor
from functools import reduce
cgpas = [3.2, 3.8, 2.9, 3.6]

passed = list(filter(lambda x: x >= 3.5, cgpas))
average = reduce(lambda a, b: a + b, cgpas) / len(cgpas)

print("Passed CGPAs:", passed)
print("Average CGPA:", round(average, 2))
