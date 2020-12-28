import random

isGuessed = False

num = random.randint(1, 10)

while isGuessed != True :
    answer = int(input("Угадай число от одного до ста\n"))
    if num == answer:
        print ("Ты угадал, молодец")
        isGuessed = True
    elif num > answer:
        print ("Твоё число меньше загаданного")
    elif answer == 0:
        isGuessed = True
    else:
        print ("Твоё число больше загаданного")

print ("Спасибо за игру")



