# Write a Python program to check whether a character is uppercase, lowercase, digit, or special
# symbol.

ch = input("Enter char :")

upperCase = {'A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

lowerCase = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z'}

digits = {'0','1','2','3','4','5','6','7','8','9'}

special_symbols = {'!','@','#','$','%','^','&','*','(',')','-','_','=', '+',
                   '[',']','{','}','\\','|',';',':',"'",'"',',','<','>','.','/','?','`','~'}

if ch in upperCase:
    print("Uppercase letter")
elif ch in lowerCase:
    print("Lowercase letter")
elif ch in digits:
    print("Digit")
elif ch in special_symbols:
    print("Special symbol")
else:
    print("Unknown or space")