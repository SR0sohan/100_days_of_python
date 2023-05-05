import random

chars = "ABCDEFGHIJKLMOPQRSUVWXYZabcdefghijklmopqrsuvwxyz1234567890!@#$%^&*_()-"
lenght = int(input("Please enter: "))
password = ""
for a in range(lenght):
    password += random.choice(chars)
print(password)