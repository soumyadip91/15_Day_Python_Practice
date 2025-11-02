# Write a Python program to print a reverse triangle pattern.
num=int(input('Enter the number : '))

for i in range(num,0,-1):
    for j in range(i):
        print("*",end="")
    print()


