# Write a Python program to determine the type of triangle (equilateral, isosceles, or scalene).

a = int(input("Enter a side 1 :"))
b = int(input("Enter a side 2 :"))
c = int(input("Enter a side 3 :"))

if(a==b==c):
    print("This is a Equilateral Triangle")
elif(a==b or 𝑏==c or a==c):
    print("This is a Isosceles Triangle \n")
elif(a!=b and b!=c and a!=c):
    print("This is a Scalene Triangle \n")