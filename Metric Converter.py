number = float(input())
merna_edinica = str(input())
izhodna_merna_edinica = str(input())

if merna_edinica == 'm' and izhodna_merna_edinica == 'cm':
    number = number * 100
elif merna_edinica == 'm' and izhodna_merna_edinica == 'mm':
    number = number * 1000
elif merna_edinica == 'cm' and izhodna_merna_edinica == 'm':
    number = number / 100
elif merna_edinica == 'cm' and izhodna_merna_edinica == 'mm':
    number = number * 10
elif merna_edinica == 'mm' and izhodna_merna_edinica == 'm':
    number = number / 1000
elif merna_edinica == 'mm' and izhodna_merna_edinica == 'cm':
    number = number / 10

print(f'{number: .3f}')

