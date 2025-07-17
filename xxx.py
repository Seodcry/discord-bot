from random import choice
password_chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Jak długie ma być wygenerowane hasło: "))
password = ""
for i in range(length):
    password += choice(password_chars)
print(password)