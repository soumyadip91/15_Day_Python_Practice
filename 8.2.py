# Write a Python program to check whether a string is a palindrome.

str=input("Enter a sting : ")

rev = str[::-1]
if str==rev:
    print("The string is palindrome")
else:
    print('The string is not palindrome')