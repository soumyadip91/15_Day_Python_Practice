# Write a Python program to check whether a triangle is valid based on its sides.

side1 = int(input("Enter a side 1 :"))
side2 = int(input("Enter a side 2 :"))
side3 = int(input("Enter a side 3 :"))

if((side1+side2)>side3 or (side1+side3)>side2 or (side2+side3)>side1):
    print("this a valid triange \n")
else:
    print("this a invalid triange \n")