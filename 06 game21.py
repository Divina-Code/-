import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED + 'Красный текст')



player1 = random.randint(2, 11)
player1Name = input("Введи своё имя  ")
print(player1, "= твоя карта")


inGame1 = True


while inGame1:

    #ПРЕДЛАГАЕМ КАРТУ 1-МУ игроку
    if inGame1:
        take_card: str = str(input(player1Name+", будешь брать карту? Да\Нет  "))
        if take_card == "Да":
            kard1 = random.randint(2, 11)
            print("карта = ", kard1)
            player1 = kard1 + player1
            print(player1Name, ", теперь у тебя очков", player1)
        elif take_card == "Нет":
            inGame1 = False
        else:
            print("Я тебя не понял")
        if player1 > 21:
            print(player1Name+", ты проиграл")
            inGame1 = False
        elif player1 == 21:
            print(player1Name+", ты победил!!!")

colorama.init()
print(Fore.BLUE + 'Синий текст')


inGame2 = True


player2 = random.randint(2, 11)
player2Name = input("Введи своё имя  ")
print(player2, "= твоя карта")

while inGame2:

    #ПРЕДЛАГАЕМ КАРТУ 2-МУ игроку
    if inGame2:
        take_card2: str = str(input(player2Name+", будешь брать карту? Да\Нет  "))
        if take_card2 == "Да":
            kard2 = random.randint(2, 11)
            print("карта = ", kard2)
            player2 = kard2 + player2
            print(player2Name, ", теперь у тебя очков", player2)
        elif take_card2 == "Нет":
            inGame2 = False
        else:
            print("Я тебя не понял")
        if player2 > 21:
            print(player2Name+", ты проиграл")
            inGame2 = False
        elif player2 == 21:
            print(player2Name+", Ты победил")
if player1 > player2:
    print("Победил, "+player1Name)
else:
    print("Победил, "+player2Name)

