slova = input("Введите несколько слов и я проверю палендром ли он  ")
slova = slova.upper()
slova = slova.split(" ")


for slovo in slova:
    a = (slovo[::-1])
    if slovo == a:
        print(slovo, " это палиндром")
else:
    print(slovo, "это не палиндром")

