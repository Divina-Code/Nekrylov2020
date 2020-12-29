z = input("Скажи слово, желательно палиндром       ").lower()
z = z.split(" ")
print(z)
for c in z:
    z1 = c[::-1].lower()
    if c.lower() == z1:
        print("Молочина, ввел палиндром")
    else:
        print("Это не палиндром!")
