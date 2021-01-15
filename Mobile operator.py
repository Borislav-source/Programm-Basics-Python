srok_contrackt = input()
type_of_contract = input()
dobaven_internet = input()
months_count = int(input())

if srok_contrackt == 'one':
    if type_of_contract == 'Small':
        sum = months_count * 9.98
    elif type_of_contract == 'Middle':
        sum = months_count * 18.99
    elif type_of_contract == 'Large':
        sum = months_count * 25.98
    elif type_of_contract == 'ExtraLarge':
        sum = months_count * 35.99
elif srok_contrackt == 'two':
    if type_of_contract == 'Small':
        sum = months_count * 8.58
    elif type_of_contract == 'Middle':
        sum = months_count * 17.09
    elif type_of_contract == 'Large':
        sum = months_count * 23.59
    elif type_of_contract == 'ExtraLarge':
        sum = months_count * 31.79

if dobaven_internet == 'yes':
    if (sum / months_count) <= 10:
        sum += months_count * 5.5
    elif (sum / months_count) <= 30:
        sum += months_count * 4.35
    elif (sum / months_count) > 30:
        sum += months_count * 3.85

if srok_contrackt == 'two':
    sum -= (sum * 0.0375)

print(f"{sum:.2f} lv.")
