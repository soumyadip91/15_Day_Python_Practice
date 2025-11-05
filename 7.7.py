# Write a Python program to sort a dictionary by key.

my_dict = {'banana': 3, 'apple': 5, 'cherry': 2, 'date': 8}

# short by key
sorted_dict = dict(sorted(my_dict.items()))

print("Original Dictionary:", my_dict)
print("Sorted Dictionary (by key):", sorted_dict)

# by valu 
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Original Dictionary:", my_dict)
print("Sorted Dictionary (by value):", sorted_by_value)






# NOTES :
# my_dict.items() → gives a list of (key, value) pairs.
# key=lambda item: item[1] → tells Python to sort using the value part.
# dict() → converts the sorted pairs back into a dictionary.