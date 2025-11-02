# Write a Python program to remove duplicates from a list.
l1 = [2,5,5,6,8,8,2,7]

unique_numbers = list(dict.fromkeys(l1))
print(unique_numbers)