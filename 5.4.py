#  Write a Python program to calculate the sum of elements in a list.


# using sum(list_name) method
l1 = [2,5,4,8,5,1,9,3]
# num=sum(l1)
# print(f"the sum of list {num}")

#using loop

sum=0
len1=len(l1)
for i in range(len1):
    sum=sum+l1[i]
print(f"The sum of elements in loop {sum}")