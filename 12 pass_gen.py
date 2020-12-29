import random
letters = list('avcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ')
symb = list('+-/*!&$#?=@<>')
length = input("какую длину пароля делать?         ")
number = input("кол-во паролей?          ")
number = int(number)
length = int(length)
for z in range(number):
    password = ""
for x in range(length):
    password += random.choice(letters + symb)
    print(password)
