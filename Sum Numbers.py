number = int(input())
sum = 0
while True:
    n = int(input())
    sum += n
    if sum >= number:
        break
print(sum)