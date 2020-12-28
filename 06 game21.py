import random

player1 = random.randint(2, 11)
player1Name = input("введи своё имя  ")
print(player1, "= твоя карта")
player2 = random.randint(2, 11)
player2Name = input("введи своё имя  ")
print(player1, "= твоя карта")

inGame1 = True
inGame2 = True

while inGame1 and inGame2:

    #ПРЕДЛАГАЕМ КАРТУ 1-МУ игроку
    if inGame1 and inGame2:
        take_card = input("Будешь брать карту? [Да\Нет]  ")
        if take_card == "Да":
            kard1 = random.randint(2, 11)
            print("карта = ", kard1)
            player1 += kard1
            print(player1Name, "Теперь у тебя очков", player1)
        elif take_card == "Нет":
            inGame1 = False
        else:
            print("Я тебя не понял")

            #ПРЕДЛАГАЕМ КАРТУ 2-МУ ИГРОКУ
        take_card = input("Будешь брать карту? [Да\Нет]  ")
        if take_card == "Да":
            kard2 = random.randint(2, 11)
            print("карта = ", kard2)
            player2 += kard2
            print(player2Name, "Теперь у тебя очков", player2)
        elif take_card == "Нет":
            inGame2 = False
        else:
            print("Я тебя не понял")
# ИЩЕМ ПОБЕДИТЕЛЯ
if player1 == 21:
    print(player1Name, "Ты победил")
elif player1 > player2:
    print(player1Name, "Ты победил")
else:
    print(player2Name, "Ты победил")


