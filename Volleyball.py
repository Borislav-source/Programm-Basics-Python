year = str(input())
holidays_count = int(input())
weekends_of_traveling = int(input())

games_in_Sofia = (48 - weekends_of_traveling) *3/4
games_in_selo = weekends_of_traveling
games_in_holidays = holidays_count * 2/3
games_in_total = games_in_Sofia + games_in_selo + games_in_holidays

if year == 'leap': bonus = games_in_total * 0.15
else: bonus = 0
games = bonus + games_in_total
import math
print(math.floor(games))
