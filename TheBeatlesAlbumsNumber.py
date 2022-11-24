
answer = int(input("Ile albumów studyjnych nagrał zespół The Beatles?"))

while answer != 12:
    if answer < 12:
      print("więcej")
    elif answer > 12:
      print("mniej")
    answer = int(input("Ile albumów studyjnych nagrał zespół The Beatles?"))
if answer == 12:
      print("Brawo")    
