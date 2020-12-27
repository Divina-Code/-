import random
a = int(random.randint(0, 10))
isGuessed = False

while  isGuessed != True:

    game = "\nугадай число от 0 до 10\n"

    answer = input(game)

    if answer < a:
        print("Ваше число меньше загаданного, попробуйте ещё раз")
    elif answer > a:
        print("Ваше число больше загаданного, попробуйте ещё раз")
    else:
        print("Вы угадали")
        isGuessed = True

print("спасибо за игру")



