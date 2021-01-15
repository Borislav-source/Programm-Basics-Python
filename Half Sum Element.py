number = int(input())
sum = 0
a = 0

for i in range(0, number):
    n = int(input())
    sum += n
    if n >= a: a = n
sum2 = sum - a
sum3 = a - sum2
if sum2 == a:
    print(f'''Yes
Sum = {sum2}''')
else:
    print(f'''No
Diff = {abs(sum3)} ''')