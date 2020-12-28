import random

player1 = random.randint(2, 11)
print("Твоя карта = ", player1)
player2 = random.randint(2, 11)
print("Твоя карта = ", player2)


inGame1 = True #Играт ли игрок1 или уже закончил




while inGame1:

    #ПРЕДЛАГАЕМ КАРТУ 1-МУ игроку
    if inGame1:
        take_card = input("Будешь брать карту? [ДА\НЕТ]")
        if take_card == "ДА":
            kard1 = random.randint(2, 11)
            print("карта = ", kard1)
            player1 += kard1
            print("Теперь у тебя очков", player1)
        elif take_card == "НЕТ":
            inGame1 = False
        else:
            print("Я тебя не понял")

    #Проверяем, не перебрал ли игрок карт
    if player1>=21:
        inGame1 = False

print("Игра окончена")

#ИЩЕМ ПОБЕДИТЕЛЯ
if player1 <= 21:
    print("Ты победил! Ура!")
else:
    print("Ты проиграл, увы")
