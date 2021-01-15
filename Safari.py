budget = float(input())
liters_gas = float(input())
day = input()
money_for_gas = liters_gas * 2.10
sum = money_for_gas + 100
if day == 'Saturday' :
    sum = sum * 0.9
elif day == 'Sunday':
    sum = sum * 0.8

total = budget - sum

if total >= 0:
    print(f"Safari time! Money left: {total:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(total):.2f} lv.")