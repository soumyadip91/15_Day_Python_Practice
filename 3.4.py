# Write a Python program to print the multiplication table of a number.

num1=int(input("Enter of table : "))
for i in range(1,11):
    print(f"\t {num1} x {i} = {num1*i}")