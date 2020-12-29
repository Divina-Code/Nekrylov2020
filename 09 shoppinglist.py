list = False #продолжительность цикла
productl = [          ]
while list != True:
    answer = int(input("добавить продукт в список:[1], удалить:[2] или посмотреть весь список?:[3]"))
    if answer == 1:
        product  = input("what do you want to add?     ")
        productl.append(product)
    elif answer == 2:
        delete = int(input("specify what you want to remove from the list   "))
        productl.pop(delete)
    elif answer == 3:
        print(productl)
else:
    print("choose 1, 2 or 3 ")


