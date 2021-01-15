budget = float(input())
season = str(input())
amount_fisherman = int(input())
if season == 'Spring':
    if amount_fisherman <= 6: price = 3000 * 0.9
    elif amount_fisherman >= 7 and amount_fisherman <= 11 : price = 3000 * 0.85
    elif amount_fisherman >= 12: price = 3000 * 0.75
if season == 'Summer':
    if amount_fisherman <= 6: price = 4200 * 0.9
    elif amount_fisherman >= 7 and amount_fisherman <= 11 : price = 4200 * 0.85
    elif amount_fisherman >= 12: price = 4200 * 0.75
if season == 'Autumn':
    if amount_fisherman <= 6: price = 4200 * 0.9
    elif amount_fisherman >= 7 and amount_fisherman <= 11 : price = 4200 * 0.85
    elif amount_fisherman >= 12: price = 4200 * 0.75
if season == 'Winter':
    if amount_fisherman <= 6: price = 2600 * 0.9
    elif amount_fisherman >= 7 and amount_fisherman <= 11 : price = 2600 * 0.85
    elif amount_fisherman >= 12: price = 2600 * 0.75
if season != 'Autumn' :
    if amount_fisherman % 2 == 0:price = price * 0.95
else: price = price
result = abs(budget - price)
if budget >= price : print(f"Yes! You have{result: .2f} leva left.")
else: print(f"Not enough money! You need{result: .2f} leva.")