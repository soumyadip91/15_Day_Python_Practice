# Write a Python function to calculate the factorial of a number
num=int(input("Enter num :"))
# f=1
# def fact(n):
#     if n==0 or n==1:
#         f=1
#         return f
#     else:
#         for i in range(n):
#             f=f*i

def fec(num):
    if num==0 or num ==1:
        f=1
        return f
    else:
        return num*fec(num-1)
    
    
c= fec(num)
print(f"The fectorial of {num} is {c}")