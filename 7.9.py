# Write a Python program to create a nested dictionary and access its elements.
students = {
    "student1": {"name": "Soumyadip", "age": 22, "course": "BTech"},
    "student2": {"name": "Akshat", "age": 21, "course": "BCA"},
    "student3": {"name": "Utsav", "age": 22, "course": "MCA"}
}

print("Complete Dictionary:")
print(students)

print("\nAccessing Elements:")
print("Student1 Name:", students["student1"]["name"])
print("Student2 Age:", students["student2"]["age"])
print("Student3 Course:", students["student3"]["course"])

print("\nAll Student Names:")
for key in students:
    print(students[key]["name"])
