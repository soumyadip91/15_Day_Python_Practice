# Write a Python program to find the sum of digits of a given number.

num=int(input("Enter 3 degit number :"))
num2=num
sum=0
for i in range(1,4):
    deg=num%10
    sum=sum+deg
    num=num//10
print(f"the sum of degetes of {num2} is {sum}")