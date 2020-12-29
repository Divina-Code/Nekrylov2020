from random import randint as ri
inGame1 = True #играет ли игрок или уже закончил#
inGame2 = True #играет игрок или уже закончил#

player1 = ri(1, 11) #очки игрока1
player2 = ri(1, 11) #счет игрока2
print("player1 ur score is: ", player1)
print("player2 ur score is: ", player2)

while inGame1 or inGame2:
    #предлагаем карту игроку
    if inGame1:
        take_card = input("player1 do u wanna take card? [Yes/No]")
        take_card = input("player2 do u wanna take card? [Yes/No]")


        if take_card == "Yes":
            player1 += ri(1, 11)
            print("now ur score is  ", player1)

        elif take_card == "No":
            print("Ok")
            inGame1 = False
        else:
            print("please repeat")
        if player2:
            
            if player1 > 21:
                inGame1 = False
                print("Game over")

            if player1 == 21:
                print("You Win!")
            else:
                print("You Lose. Try again later")



    if inGame2:
        take_card2 = input("do u need a card? [Yes/No]   ")
        if take_card2 == "Yes":
            player2 += ri(1, 11)
            print("now ur score is: ", player2)
        elif take_card2 == "No":
            inGame2 = False
        else:
            print("repeat please")
            if take_card2 >= 21:
                print("Game over")
                inGame2 = False
                if take_card2 == 21:
                    print("You Win!")
inGame1 = False
inGame2 = False

