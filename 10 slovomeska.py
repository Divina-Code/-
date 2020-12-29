from random import choice, shuffle


words = ['антарктида', 'амплитуда', 'локомотив', 'индустриализация', 'процессор']

word = choice(words).lower()


shuffle_word = list(word)
shuffle(shuffle_word)


game = True

while game:
    user_word = input("Угадай слово: "+ ''.join(shuffle_word) +'\t')

    if user_word == word:
        print("Угадал")
        word = choice(words).lower()
        shuffle_word = list(word)
        shuffle(shuffle_word)
    else:
        print("Не угадал")
