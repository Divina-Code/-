
import random

words = ['антарктида', 'амплитуда', 'локомотив', 'индустриализация', 'процессор']

word = random.choice(words).lower() #выбор слова из предложенных

#замена слова на "_"
letters = []
for a in word:
    letters.append("_")

print(' '.join(letters))

lives = 5 # жизни игрока
print("У тебя жизней = ", lives)

game = True

while game:
    answer = input("Букву или слово:  ")
    for a in range(len(word)):
        if answer == word[a]:
            letters[a] = word[a]
            print(''.join(letters))
        elif answer == word:
            print("Ты выйграл")
            game = False
    lives -= 1
    print("теперь у тебя жизней = ", lives)
    if lives == 0:
        print("У тебя закончились жизни, ты проиграл")
        game = False




