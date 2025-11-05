# Write a Python program to check if a key exists in a dictionary

num_dist ={
    "a" : 5,
    "b" : 7,
    "c" : 9,
    "f":14,
    "g":17,
    "h":19
}

K=input("Enter key : ")
if K in num_dist.keys():
    print("the key is avaliable")
else:
    print("the key is not avaliable")