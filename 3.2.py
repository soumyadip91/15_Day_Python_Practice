# Write a Python program to print all even numbers between 1 and 100
num = int(input("Enter n :"))
for i in range(1,num+1):
    if(i%2==0):
        print(i)
    else:
        continue