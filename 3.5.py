# Write a Python program to find the factorial of a number.
num = int(input("Enter a number :"))
factoriacl =1
for i in range (1,num+1):
    factoriacl=factoriacl*i
print(f"The factorial of {num} is {factoriacl}")