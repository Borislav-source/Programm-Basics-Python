number_of_pages = int(input())
pages_for_1_hour = int(input())
days = int(input())

time_book: float = number_of_pages / pages_for_1_hour
time_per_day: float = time_book / days

print(time_per_day)