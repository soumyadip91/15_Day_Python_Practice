# Write a recursive Python function to reverse a string.
str =input("Enter a string : ")

def revofStr(str):
    if len(str)==0:
        return str
    else:
        return revofStr(str[1:])+str[0]
    
print(f"The reverse of  string : {revofStr(str)}")