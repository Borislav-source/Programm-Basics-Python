name = input()
studet_class_year = 1
bad_grade = 0
total = 0
while studet_class_year <= 12 and bad_grade != 2:
    grade = float(input())
    if grade >= 4:
        total += grade
        studet_class_year += 1
    else:
        bad_grade += 1

if bad_grade == 2:
        print(f'{name} has been excluded at {studet_class_year} grade')
else: average_garde = total / 12; print(f'{name} graduated. Average grade: {average_garde:.2f}')

