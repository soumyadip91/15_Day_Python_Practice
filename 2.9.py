# Write a Python program to calculate the grade of a student based on marks.

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks >= 40:
    grade = "E"
elif marks >= 0 and marks <= 40:
    grade = "F"
else:
    print("Invalid inputs \n")
print(f"Your Grade is: {grade}")
