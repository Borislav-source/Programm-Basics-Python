n = int(input())
left_sum = 0
right_sum = 0

for i in range(1, n + 1):
    left_digit1 = int(input())
    left_sum += left_digit1
for j in range(1, n + 1):
    right_digit1 = int(input())
    right_sum += right_digit1
if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    result = right_sum - left_sum
    print(f'No, diff = {abs(result)}')