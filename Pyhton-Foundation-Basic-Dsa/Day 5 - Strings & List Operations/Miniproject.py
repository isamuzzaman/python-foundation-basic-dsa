# Word Counter Tool
sentence=input("Enter a sentence :")
total_words=sentence.split()

vowels="aeiouAEIOU"
total_vowels=0
for ch in sentence:
    if ch in vowels:
        total_vowels+=1

print("Total Characters :",len(sentence))
print("Total words :",len(total_words))
print("TOtal Vowels:",total_vowels)
        