

d = {"t" : "b"}
s = input("Нажмите [1] чтобы добавить слово, Нажмите [2] чтобы открыть список, Нажмите [3] чтобы начать играть    ")
if s == "L":
    a = [input("Скажите слово и перевод   ").split()]
    if len(a) == 2:
        name = a[0]
        translate = a[1]
    if d.get(name) == None:
        d[name] = translate
    else:
                print("это слово уже есть ")
else:
    print("Попробуй ещё раз ")
