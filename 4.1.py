# Write a Python program to print numbers in a right-angled triangle pattern

num=int(input('Enter the number : '))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



    # to remove next line we can use print()