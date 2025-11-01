# Write a Python program to count the number of digits in a number.

num = int(input("Enter a number: "))
while 1 :
    count = 0
    while num > 0:
        count += 1
        num //= 10
    print("Number of digits:", count)
    break
