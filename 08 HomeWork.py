inList = False 
productlist = []
while inList != True:
    answer = int(input("добавить продукт в список:[1], удалить:[2] или посмотреть весь список?:[3]  "))
    if answer == 1:
        product = input("что ты хочешь добавить?  ")
        productlist.append(product)

    elif answer == 2:
        delete = int(input("что ты хочешь удалить?  "))
        productlist.pop(delete)

    elif answer == 3:
        print(productlist)
else:
    print("выберите 1, 2 или 3")


