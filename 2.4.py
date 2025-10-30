# Write a Python program to check if a character is a vowel or consonant.

charecter = input("Enter a char: ")

# if ((charecter == 'A' or charecter == 'E' or charecter == 'I' or charecter == 'O' or charecter == 'U') or 
#     (charecter == 'a' or charecter == 'e' or charecter == 'i' or charecter == 'o' or charecter == 'u')):
#     print(f"{charecter} is a vowel\n")
# else:
#     print(f"{charecter} is a consonant\n")



# alternative approtch  using MEMBERSHIP OPERATOR

vowels ={'a','e','i','o','u','A','E','I','O','U'}

if charecter in vowels:
    print(f"{charecter} is a vowel\n")
else:
    print(f"{charecter} is a consonant\n")