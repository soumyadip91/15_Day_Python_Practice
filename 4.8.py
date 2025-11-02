#Write a Python program to check whether a number is a palindrome.
num = int(input("Enter number"))

temp =num
rev=0

while num>0:
    deg=num%10
    rev=rev*10+deg
    num=num//10
if (temp==rev):
    print("The number is palindrome \n")
else:
    print("The number is not palindrome \n")