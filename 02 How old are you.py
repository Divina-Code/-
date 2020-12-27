print("Hello, user!")


user_name = input("What is your name?   ")
print("Hello,", len(user_name), 'letters')


user_eayr = int (input("Whan you was born?   "))
if len(str(user_eayr)) == 4:
    print("nise eyar,", user_eayr)
    print(2020-user_eayr)
else:
    print("you make mistake")
