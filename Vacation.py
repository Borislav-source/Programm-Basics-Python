money_needed = float(input())
current_money = float(input())
number_of_spend = 0
number_of_days = 0
while number_of_spend < 5 and current_money < money_needed:
    spend_or_save = input()
    money = float(input())
    number_of_days += 1
    if spend_or_save == 'save':
        number_of_spend = 0
        current_money += money
    elif spend_or_save == 'spend':
        current_money -= money
        number_of_spend += 1
        if current_money < 0:
            current_money = 0

if number_of_spend >= 5:
    print("You can't save the money.")
    print(number_of_days)
elif current_money >= money_needed:
    print(f'You saved the money for {number_of_days} days.')
