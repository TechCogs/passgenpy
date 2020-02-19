import random

VERSION = 1.0

password = ""
length = 0
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["@", "^"]

print("passgenpy v" + str(VERSION))
print("")
try:
    length = int(input("Enter desired password length>"))
except:
    print("Usage:  Enter a number")
    exit(1)
for l in range(length):
    charType = random.randrange(100)
    if charType < 25:
        password += str(random.choice(numbers))
    elif charType >= 25 and charType < 50:
        password += random.choice(symbols)
    else:
        if random.randrange(100) < 50:
            password += random.choice(letters).upper()
        else:
            password += random.choice(letters)
print("New password:  " + password)
