#Write a Python program to calculate simple interest.

P=int(input("Enter a principal : "))
R=int(input("Enter a rate : "))
T=int(input("Enter a time(years) : "))

print(f"The simple interest of you capital :{(P*R*T)/100}")