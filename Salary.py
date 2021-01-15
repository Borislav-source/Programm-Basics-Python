n_open_tabs = int(input())
salary = float(input())

for i in range(0, n_open_tabs):
    site = input()
    if site == 'Facebook': salary -= 150
    if site == 'Instagram': salary -= 100
    if site == 'Reddit': salary -= 50
    if salary <= 0: break

if salary <= 0:
    print('You have lost your salary.')
else:
    print(f'{salary:.0f}')