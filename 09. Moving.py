width_of_the_apartment = int(input())
length_of_the_apartment = int(input())
hight_of_the_apartment = int(input())
inpt = input()
free_area = width_of_the_apartment * length_of_the_apartment * hight_of_the_apartment
needed_area_for_boxes = 0
input1 = ''

while inpt != 'Done':
    number_of_boxes = int(inpt)
    needed_area_for_boxes += number_of_boxes
    if needed_area_for_boxes > free_area:break
    inpt = input()

if free_area < needed_area_for_boxes:
    the_sum = needed_area_for_boxes - free_area
    print(f'No more free space! You need {the_sum} Cubic meters more.')
else: the_sum = free_area - needed_area_for_boxes; print(f'{the_sum} Cubic meters left.')


