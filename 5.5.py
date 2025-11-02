# Write a Python program to count even and odd numbers in a list.
l1 = [2,5,4,8,5,1,9,3]  # given list

count=0
len1=len(l1)
for i in range(len1):
    if l1[i]%2==0:
        count=count+1
print(f"The no of even elements in loop {count}\n The no of odd elements {len1-count}")