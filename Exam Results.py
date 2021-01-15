import math
text = input()
points = 0
while text != 'Midnight':
    for i in range(0, 6):
        a = int(input())
        if a < 0:
            print(f'{text} was cheating!')
            break
        points += a
    b = math.floor(points / 6)
    b *= 0.06
    if b < 3:
        b = 2
    if b >= 5 and a > -0.1 and b <= 6:
        print(f'''===================
|   CERTIFICATE   |
|    {b:.2f}/6.00    |
===================
Issued to {text}
''')
    if b < 5 and a > -0.1:
        print(f'{text} - {b:.2f}')
    points = 0
    text = input()
