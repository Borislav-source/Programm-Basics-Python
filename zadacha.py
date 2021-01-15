text = input()
sum = 0
for k in range(0, len(text)):
    if text[k] == 'a':
        sum += 1
    elif text[k] == 'e':
        sum += 2
    elif text[k] == 'i':
        sum += 3
    elif text[k] == 'o':
        sum += 4
    elif text[k] == 'u':
        sum += 5
print(sum)