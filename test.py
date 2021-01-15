inpt = input()
max = -1000000000000000

while inpt != 'Stop':
    num = int(inpt)
    print(num)
    if num > max:
        max = num
    inpt = input()

print(max)