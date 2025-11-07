# Write a recursive Python function to calculate the factorial of a number.
num=5

def fac(n):
    if n==0 or n==1:
        val=1
        return val
    else:
        return n*fac(n-1)
valu=fac(num)
print(f"factorial is {valu}")