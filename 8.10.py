# Write a Python program to find all substrings of a given string

text = input("Enter a string: ")

print("All substrings are:")

for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        print(text[i:j])
