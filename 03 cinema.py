user_name = input("whats ur name?       ")
print("hello" , user_name, "in your name ", len(user_name), 'letters')
user_year = int(input("enter the year of your birth    "))
if 2020 - user_year >= 18:
    print('do u wanna watch an action movie')
else:
    print('lets go watch cartoon')
