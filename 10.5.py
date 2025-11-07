# Write a recursive Python function to find the power of a number.

def power(base,expo):
    if expo==0:
        return 1
    else:
        return base*power(base,expo-1)
    
a=int(input("Enter base : "))
b=int(input("Enter expo : "))

print(power(a,b))