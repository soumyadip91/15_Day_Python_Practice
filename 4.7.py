# Write a Python program to find the GCD of two numbers.

num1=int(input("Enter num 1 :"))
num2=int(input("Enter num 2 :"))


while(num2 !=0):
    num1,num2=num2,num1%num2

print(f"The GCD of the given numbers is: {num1}")