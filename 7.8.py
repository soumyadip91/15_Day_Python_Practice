# Write a Python program to count word frequency in a given string using a dictionary

from collections import Counter

text = input("Enter a string: ").lower().split()
word_count = Counter(text)

print("\nWord Frequency:")
for word, freq in word_count.items():
    print(f"{word} : {freq}")
