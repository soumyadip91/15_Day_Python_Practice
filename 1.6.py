#Write a Python program to find the largest among three numbers

num1=int(input("Enter a number : "))
num2=int(input("Enter a number : "))
num3=int(input("Enter a number : "))
if num1>num2:
    large=num1
else:
    large=num2
if large>num3:
    lar=large
else:
    lar=num3
print(f"The largest number : {lar}")