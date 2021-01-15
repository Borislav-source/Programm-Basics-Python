flowers_kind = str(input())
amount_flowers = int(input())
budget = float(input())
rose = 5
dalia = 3.8
lale = 2.8
narcis = 3
gladiola = 2.5
if flowers_kind == 'Roses':
    if amount_flowers <= 80 : price = amount_flowers * rose
    else: price = (amount_flowers * rose) * 0.9
if flowers_kind == 'Dahlias':
    if amount_flowers <= 90 : price = amount_flowers * dalia
    else:price = (amount_flowers * dalia) * 0.85
if flowers_kind == 'Tulips':
    if amount_flowers <= 80 : price = amount_flowers * lale
    else:price = (amount_flowers * lale) * 0.85
if flowers_kind == 'Narcissus':
    if amount_flowers < 120 : price = (amount_flowers * narcis) + (amount_flowers * narcis) * 0.15
    else:price = amount_flowers * narcis
if flowers_kind == 'Gladiolus':
    if amount_flowers < 80 : price = (amount_flowers * gladiola) + (amount_flowers * gladiola) * 0.2
    else: price = amount_flowers * gladiola
result = abs(budget - price)
if budget >= price : print(f"Hey, you have a great garden with {amount_flowers} {flowers_kind} and{result: .2f} leva left.")
else: print(f"Not enough money, you need{result: .2f} leva more.")