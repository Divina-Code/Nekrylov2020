print("hello user")
user_name = input("whats ur name?       ")
print("hello" , user_name, "in your name ", len(user_name), 'letters')
user_year = int(input("enter the year of your birth    "))
if len(str(user_year)) == 4:
    print("nice year,", user_year)
    print(2020 - user_year)
else:
    print("u make mistake")
