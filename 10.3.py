# Write a recursive Python function to find the sum of digits of a number.
sum=0

num=int(input("Enter a 3 degit number : "))
def sumofDeg(num):
    if num==0:
        return 0
    else:
        return (num%10)+sumofDeg(num//10)

sum=sumofDeg(num)
print(f"The sumof deg : {sum}")
    