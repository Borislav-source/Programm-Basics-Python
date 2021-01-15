sum = 0
while True:
    input_money = input()
    if input_money == 'NoMoreMoney': break
    input_money = float(input_money)
    if input_money < 0: print('Invalid operation!'); break
    sum += input_money
    print(f'Increase: {input_money:.2f}')
print(f'Total: {sum:.2f}')