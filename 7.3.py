# Write a Python program to find the sum of all values in a dictionary.

num_dist ={
    "a" : 5,
    "b" : 7,
    "c" : 9,
    "f":14,
    "g":17,
    "h":19
}

sum=0

for key in num_dist:
    sum=sum+num_dist[key]

print(f"The sum of all elements of dist : {sum}")