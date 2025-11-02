# Write a Python program to find the second largest element in a list.
l1 = [2,5,4,8,5,1,9,3] 
l=len(l1)-2
l1.sort()  
print(f"The secound largest number = {l1[l]}")