# What is a String

s = "Python"
print(s[0])   # P
print(len(s))

# String Traversal
for ch in s:
    print(ch)

# String Methods (Important)
text = "data science"

print(text.upper())
print(text.lower())
print(text.title())
print(text.count("a"))
print(text.replace("data", "AI"))

# String Slicing
word = "programming"
print(word[0:4])   # prog
print(word[::-1])  # reverse

# String Comparison
a = "python"
b = "Python"

print(a == b)
