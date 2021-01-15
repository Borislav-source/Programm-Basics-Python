magic_number = int(input())
combinations = 0
for i in range(0, magic_number + 1):
    for k in range(0, magic_number + 1):
        for m in range(0, magic_number + 1):
            if i + k + m == magic_number:
                combinations += 1
print(combinations)