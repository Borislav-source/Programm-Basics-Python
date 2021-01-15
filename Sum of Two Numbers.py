num1 = int(input())
num2 = int(input())
magig_num = int(input())
flang = False
combination = 0
for i in range(num1, num2 + 1):
    for k in range(num1, num2 + 1):
        combination += 1
        if i + k == magig_num:
            print(f"Combination N:{combination} ({i} + {k} = {magig_num})")
            flang = True
            break
    if flang:
        break
if flang == False:
    print(f"{combination} combinations - neither equals {magig_num}")
