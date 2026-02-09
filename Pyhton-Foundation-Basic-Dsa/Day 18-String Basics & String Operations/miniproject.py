# Word Analyzer
s=input("Enter a string :")
count=0
for ch in s:
    if ch in "AEIOUaeiou":
        count=count+1
print("Vowels :",count)
print("Characters :",len(s))
print("Words :",len(s.split()))
print("Reverse :",s[::-1])    