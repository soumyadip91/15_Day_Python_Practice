# Write a Python program using a lambda function to add two numbers.

add = lambda a,b: a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum:", add(x, y))