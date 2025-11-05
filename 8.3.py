# Write a Python program to find the frequency of each character in a string.
from collections import Counter

str=input("Enter a sting : ")
l1= list(str)
freq=Counter(l1)
print(freq)
