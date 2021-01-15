budget = float(input())
number_statisti = int(input())
price_clothes = float(input())
decore = budget * 0.1
if number_statisti > 150: price_clothes = price_clothes - (price_clothes * 0.1)
total_price = (number_statisti * price_clothes) + decore
nujni_money: abs = abs(budget - total_price)
if total_price > budget: print(f'''Not enough money!
Wingard needs{nujni_money: .2f} leva more. ''')
else: print(f'''Action!
Wingard starts filming with{nujni_money: .2f} leva left.''')