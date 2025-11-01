# Write a Python program to reverse a number using loops.
num=int(input("Enter a 3 degit number : "))
rev=0
for i in range(1,4):
   digit = num % 10
   rev = rev * 10 + digit
   num //= 10
print(f"{num} -> {rev}")