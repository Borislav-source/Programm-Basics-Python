budget = float(input())
sum = 0
products_count = 0

while budget >= sum:
    name = input()
    if name == 'Stop':
        break
    price = float(input())
    products_count += 1
    if products_count % 3 == 0:
        price /= 2
    sum += price

if budget >= sum:
    print(f'You bought {products_count} products for {sum:.2f} leva.')
else:
    total = sum - budget
    print(f'''You don't have enough money!
You need {total:.2f} leva!''')
