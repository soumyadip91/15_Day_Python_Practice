# Write a Python program to find the frequency of each element in a list.

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of each element:")
for key, value in frequency.items():
    print(f"{key} : {value}")
