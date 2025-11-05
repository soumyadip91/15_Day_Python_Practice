# Write a Python program to check if a string contains both letters and numbers.

text = input("Enter a string: ")

has_letter = False
has_digit = False

for ch in text:
    if ch.isalpha():
        has_letter = True
    elif ch.isdigit():
        has_digit = True

if has_letter and has_digit:
    print("The string contains both letters and numbers.")
else:
    print("The string does not contain both.")