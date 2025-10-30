# Write a Python program to check whether a number is divisible by both 5 and 11.

num = int(input("Enter a num : "))
if (num%5==0 and num%7==0):
    print(f"The number {num} is devisible by 5 & 7 both \n")
else:
    print(f"The number {num} is not devisible by 5 & 7 both \n")