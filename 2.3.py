# Write a Python program to determine whether a year is a leap year.
year = int(input("Enter year : "))
if((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
    print(f"{year} is leap year \n")
else:
    print(f"{year} is not a leap year\n")
