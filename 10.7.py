# Write a Python program using lambda and filter to find even numbers in a list.

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)