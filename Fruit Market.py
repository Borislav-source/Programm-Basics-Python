price_qgoda = float(input())
number_banani = float(input())
number_portokali = float(input())
number_malini = float(input())
number_qgoda = float(input())

price_malini = price_qgoda / 2
price_portokali = price_malini * 0.6
price_banani = price_malini * 0.2

total = number_qgoda * price_qgoda + number_banani * price_banani + number_malini * price_malini + number_portokali * price_portokali

print(total)