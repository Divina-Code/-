isGuessed = False

while isGuessed != True:

    riddle = "\nБыло 6 друзей, на сколько равных частей надо разрезать торт, что бы всем досталось одинаковое количество торта "

    answer = input(riddle)

    if answer == "6":
        print("правельно")
        isGuessed = True
    else:
        print("ты не прав, попробуй ещё раз")
print("спасибо за игру")
