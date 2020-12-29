
import random

letters = list("abcdefghijkABCDEFGHIJK")
sym = list("`!@#$%^&*()_?><:|}{")
cifr = list("123456789")
znaki = letters+sym+cifr

length = int(input("длина пароля?\t"))

password = ''

for a in range(length):
   password += random.choice(znaki)
print(password)
