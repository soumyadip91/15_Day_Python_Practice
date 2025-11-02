# Write a Python program to generate Fibonacci series up to n terms.

n=int(input("Enter n : "))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b