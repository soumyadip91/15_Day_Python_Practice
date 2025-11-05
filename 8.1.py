# Write a Python program to count the number of vowels in a string.

str = "Soumyadip"
vow="AEIOUaeiou"
count=0

for ch in str:
    if ch in vow:
        count=count+1
    else:
        continue
print(f"no of vowels : {count}")