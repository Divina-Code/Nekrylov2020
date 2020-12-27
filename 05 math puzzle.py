isGuessed = False
while isGuessed != True:
  puzzle = "4+4*2     "
  answer = input(puzzle)
  if answer == "12":
      print("ДА, совершенно верно!")
      isGuessed = True
  else:
      print("нет, не верно")
