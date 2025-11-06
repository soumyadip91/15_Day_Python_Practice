# Write a Python function to count vowels in a string.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

string = "Hello World"
print("Number of vowels:", count_vowels(string))
