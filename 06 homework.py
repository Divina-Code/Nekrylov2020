guessed = False
while guessed != True:
    answer = int(input("the number is"))
    if answer == 55:
        print("lucky")
        guessed = True
    elif answer > 55:
        print('the number is smaller')
    else:
        print('the number is bigger')
print("well done!")
