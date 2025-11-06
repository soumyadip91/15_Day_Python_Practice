# Write a Python function to find the nth Fibonacci number.

num = int(input("Enter a number :"))

def fact(num):
    if num==1 or num==0:
        val=1
        return val
    else:
        return num*fact(num-1)
    
valu=fact(num)
    
print(f" the factorial of {num} is {valu}")