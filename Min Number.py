from sys import maxsize
n = maxsize
while True:
    a = input()
    if a == 'Stop':break
    elif int(a) < int(n): n = a
print(n)