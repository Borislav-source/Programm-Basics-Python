month = str(input())
nights_count = int(input())
studio = 0
apartament = 0

if month == 'May' or month == 'October':
    if month == 'May' or month == 'October': studio = 50; apartament = 65
    if nights_count > 14: studio = studio * 0.7
    elif nights_count > 7: studio = studio * 0.95
    if nights_count > 14: apartament = apartament * 0.9
elif month == 'June' or month == 'September':
    if month == 'June' or month == 'September': studio = 75.20; apartament = 68.70
    if nights_count > 14: studio = studio * 0.8
    if nights_count > 14: apartament = apartament * 0.9
elif month == 'July' or month == 'August':
    if month == 'July' or month == 'August': studio = 76; apartament = 77
    if nights_count > 14: apartament = apartament * 0.9
bill_1 = apartament * nights_count
bill_2 = studio * nights_count
print(f'''Apartment:{bill_1: .2f} lv.
Studio:{bill_2: .2f} lv.''')