lenght = int(input())
width = int(input())
height = int(input())
percent_occupied = float(input())

volume = (lenght * width * height) / 1000
water = volume - (volume * (percent_occupied / 100))

print(water)