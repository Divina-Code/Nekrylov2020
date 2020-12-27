isGuessed = False
while isGuessed != True:
  puzzle = "хоккеистов слышен плач пропустил вратарь их.."
  answer = input(puzzle)
  if answer == "шайбу":
   print("да, ты молочина!!")
   isGuessed = True
  elif answer == "мяч":
      print("попался!!")
  else:
      print("Нет, не угадал(")

print("спасибо за игру")
