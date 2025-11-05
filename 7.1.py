# Write a Python program to create a dictionary and display its elements

person_dist= {
    "name" : "Salmon Bhai",
    "job" : "Gangstar",
    "address" : "Thane , Mumbai"
}

# print(person_dist) optional

for key in person_dist:
    print(f"{key} : {person_dist[key]}")