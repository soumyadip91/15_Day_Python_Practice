# Write a Python program to find the longest word in a string.
text = input("Enter a sentence: ")

words = text.split()  # in to list
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word
print("The longest word is:", longest)
print("Length of the word:", len(longest))
