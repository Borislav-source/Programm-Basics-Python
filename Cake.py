lenght_of_cake = int(input())
width_of_cake = int(input())
cake = lenght_of_cake * width_of_cake
eaten_pieces = 0
comand = input()
while comand != 'STOP':
    pieces = int(comand)
    eaten_pieces += pieces
    if eaten_pieces > cake:break
    comand = input()

if eaten_pieces > cake:
    rest = eaten_pieces - cake
    print(f"No more cake left! You need {rest} pieces more.")
else:
    rest = cake - eaten_pieces
    print(f"{rest} pieces are left.")