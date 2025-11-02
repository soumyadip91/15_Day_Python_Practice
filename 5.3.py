# Write a Python program to find the smallest element in a list.

l1 =[1,4,2,6,7,9,3]
#small=0
# for i in range(len(l1)):
#     if small<l1[i]:
#         continue
#     else:
#         small=l1[i]
# print(f"Largest {small} \n")

l1.sort()
print(l1[0])