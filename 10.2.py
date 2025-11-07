# Write a recursive Python function to calculate the nth Fibonacci number.
num=int(input("Entera number :"))
print("Fibbonachhi series : ")
def fab(n):
    if n<=1:
        return n
    else:
        return fab(n-2)+fab(n-1)
for i in range(num):
    print(fab(i),end=" ")