# number = float(input())
#
# while number < 1 or number > 100:
#     number = float(input())
# print(f'The number {number} is between 1 and 100')
#

number = int(input())

for i in range(1, number + 1):
    for j in range(0, i):
        print('*', end = "")
    print()
for i in range(number - 1, 0, - 1):
    for j in range(i, 0, -1):
        print('*', end="")
    print()