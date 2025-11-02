# Write a Python program to print all prime numbers between 1 and 100.

for num in range(2,101):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            break
    else:
        print(num)


# sum of prime numbers between 1-100

sum=0
for num in range(2,101):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            break
    else:
        sum=sum+num
print(f"The sum of prime numbers : {sum} \n")