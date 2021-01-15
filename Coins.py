from math import floor
resto = float(input())
coins = 0
levs = 0
sum = 0
re = int(resto)
while sum < resto:
    if resto < 1:
        levs = 0
    elif resto >= 1 and resto < 2:
        levs = 1
    elif resto >= 2:
        levs = floor(resto)
    coins = (resto - re) + 0.001
    coins = floor(coins * 100)
    if levs >= 1:
        if levs == 1:
            sum += 1
        elif levs >= 2:
            sum = (levs % 2) + floor(levs / 2)
    if coins > 0 and coins < 100:
        if coins - 50 >= 0:
            coins -= 50
            sum += 1
        if coins / 20 >= 1:
            sum += floor(coins / 20)
            coins = coins % 20
        if coins / 10 >= 1:
            sum += floor(coins / 10)
            coins = coins % 10
        if coins / 5 >= 1:
            sum += floor(coins / 5)
            coins = coins % 5
        if coins / 2 >= 1:
            sum += floor(coins / 2)
            coins = coins % 2
        if coins / 1 > 0:
            sum += (coins / 1)
    break
print(floor(sum))
