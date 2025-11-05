# Write a Python program to merge two dictionaries.

num_dist ={
    "a" : 5,
    "b" : 7,
    "c" : 9
}

num_dist2={
    "f":14,
    "g":17,
    "h":19
}
num_dist.update(num_dist2)
print(num_dist)