#  Write a Python program to capitalize the first letter of every word in a string.
text = input("Enter a string: ")

list=text.split()
list2=[]
for ch in  list:
    list2.append(ch.capitalize())

str2=' '.join(list2)

print(str2)