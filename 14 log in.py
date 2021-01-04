# user_data = {}

user_data = {
    "admin" : "ytrewq321",
    "user"  : "0000",

}

while True:
    answer = input("Вы новый[N] пользователь или существующий?[O] ").upper()
    if answer == "N":
        data = input("Введите логин и пароль").split()
        if len(data) == 2:
            login = data[0]
            password = data[1]

            #Если пользователя с таким логином ещё нет
            if user_data.get(login) == None:
                user_data[login] = password  #Добавляем пользователя в словарь

            else: #если такой пользователь уже есть в словаре
                print("Такой логин уже занят")

        else: #Если было введено больше 2х значений
            print("попробуй ещё раз")


    if answer == "O":
        data = input("Введите логин и пароль").split()
        if len(data) == 2:
            login = data[0]
            password = data[1]

            #Проверяем, совпадает ли введённый пароль с тем, что у нас записан
            #Если пользователя с таким логином ещё нет
            if user_data.get(login) == None:
                print("Такого пользователя нет, попробуй другой логин")

            else:
                if password == user_data[login]:
                    print("С возвращением,", login)
                else:
                    print("Пароль неверный")


        else: #Если было введено больше 2х значений
            print("попробуй ещё раз")

    if answer == 'D':
        login = input("Кого удалить? ")
        if user_data.get(login) == None:
            print("Такого пользователя нет, попробуй другой логин")

        else:
            user_data.pop(login)
            print(f"Пользователь {login} удалён")

    if answer == "A":
        print(*sorted(user_data.keys()), sep='\n')
