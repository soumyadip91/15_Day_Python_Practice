# Write a Python program to find the key with the maximum value in a dictionary.

num_dist ={
    "a" : 5,
    "b" : 7,
    "c" : 9,
    "f":14,
    "g":17,
    "h":19
}

larg=0

for key in num_dist:
    if larg < num_dist[key]:
        larg=num_dist[key]
    else:
        continue
print(f"The largest element in dist : {larg}")
