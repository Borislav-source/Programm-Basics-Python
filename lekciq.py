price_ekskurziq = float(input())
number_puzzels = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

puzzel_price = 2.6
puzzel_doll = 3
puzzel_bear = 4.1
puzzel_minion = 8.2
puzzel_truck = 2

income = number_bears * puzzel_bear + number_dolls * puzzel_doll + number_minions * puzzel_minion + number_puzzels * puzzel_price + number_trucks * puzzel_truck
number = number_trucks + number_puzzels + number_bears + number_minions + number_dolls

if number >= 50: income = income * 0.75

income = income * 0.9

if income > price_ekskurziq: print(f"Yes! {income - price_ekskurziq:.2f} lv left.")
else:print(f"Not enough money! {price_ekskurziq - income:.2f} lv needed.")