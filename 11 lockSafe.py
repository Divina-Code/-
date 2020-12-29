from random import randint


random_number = randint(100, 999)

code = str(random_number)





game = True
while game:
    user_number = input("Введи трёхзначное число:\t")
    right_number = 0 #Сколько цифр угадано вообще
    right_placed = 0 #сколько цифр стоит на нужном месте

    if len(user_number)!=3:
        print('Это не трёхзначное число')
    elif not user_number.isdigit():
        print("только цифры")

    elif user_number == code:
        print("Ты угадал")
        game = False
    else:
        for d in code:
            if d in user_number:
                right_number+=1

        for i in range(3):
            if user_number[i] == code[i]:
                right_placed+=1


    print("Ты угадал вот столько цифр:", right_number, 'из них правильно расположены', right_placed)
