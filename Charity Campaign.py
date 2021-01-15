number_days = int(input())
number_cooks = int(input())
number_cakes = int(input())
number_waffles = int(input())
number_pancakes = int(input())

income_for_a_day = ((number_cakes*45 + number_waffles*5.8 + number_pancakes*3.2) * number_cooks) * number_days
profit = income_for_a_day - (income_for_a_day / 8)

print(profit)


