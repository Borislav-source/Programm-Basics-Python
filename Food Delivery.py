number_pileshko = int(input())
number_riba = int(input())
number_veget = int(input())

sum1 = (number_pileshko * 10.35) + (number_riba * 12.40) + (number_veget * 8.15)
sum1 += (sum1 * 0.2) + 2.5

print(f"Total: {sum1:.2f}")