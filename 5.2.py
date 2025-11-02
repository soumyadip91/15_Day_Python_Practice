# Write a Python program to find the largest element in a list.
l1 =[1,4,2,6,7,9,3]

# large=0

# for i in range(len(l1)):
#     if large>l1[i]:
#         continue
#     else:
#         large=l1[i]
# print(f"Largest {large} \n")

l1.sort()
print(l1[6])