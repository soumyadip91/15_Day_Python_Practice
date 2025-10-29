#Write a Python program to calculate compound interest
P=int(input("Enter a principal : "))
R=int(input("Enter a rate : "))
T=int(input("Enter a time(years) : "))
A = P * (pow((1 + R / 100), T))
print(f"The compound interest of the principal : {A}")
      