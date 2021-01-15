n = int(input())
a = 0
for i in range(1, n):
    a = (a * 2) + 1
    print(a)
    if a > (n - n / 2): break
if n == 1: print(n)


