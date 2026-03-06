# Palindrome
def is_palindrome(s):
    return s == s[::-1]
# Anagram
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
# Character Frequency
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
# Remove duplicate characters
def remove_duplicates(s):
    result = ""
    
    for ch in s:
        if ch not in result:
            result += ch
            
    return result
# Reverse words in a sentence
def reverse_words(sentence):
    words = sentence.split()  
    words.reverse()            
    return " ".join(words)       