print("Hello, user!")


user_name = input("What is your name?   ")
user_eayr = int (input("Whan you was born?   "))
user_age = 2020 - user_eayr
if user_age > 18:
    print(user_name,"let's watch an action movie")
else:
    print(user_name,"let's watch a Comedy")
