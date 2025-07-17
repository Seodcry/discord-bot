from random import choice

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def password_m(length=8): 
    password = ""
    for i in range(length):
        password += choice(chars)
    return password