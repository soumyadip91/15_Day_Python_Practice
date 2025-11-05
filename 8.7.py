# Write a Python program to count uppercase and lowercase letters in a string.

str ="Soumyadip"

upr = "QWERTYUIOPLKJHGFDSAZXCVBNM"
lwr ="qwertyuioplkjhgfdsazxcvbnm"
upcount=0
lwcount=0

for ch in str:
    if ch in upr:
        upcount+=1
    elif ch in lwr:
        lwcount+=1
    else:
        continue

print(f"The upper case is {upcount} and lower cse {lwcount}")