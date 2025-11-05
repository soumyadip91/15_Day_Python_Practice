# Write a Python program to add, update, and delete dictionary elements.

num_dist ={
    "a" : 5,
    "b" : 7,
    "c" : 9
}

# add element 
num_dist["d"]=int(input("Enter a number : "))
print(num_dist)

# updata (delete)
c=input("Enter key to delete :")
val = num_dist.pop(c)
print(f"{val} is been deleted")

# update (mearge two dist)
num_dist2={
    "f":14,
    "g":17,
    "h":19
}
num_dist.update(num_dist2)
print(num_dist)

# clear all item from dist
num_dist.clear()
print(num_dist)