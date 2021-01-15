import math
students_count = int(input())
season = int(input())
season_count = 0
for i in range(0, season):
    season_count += 1
    first_exam = math.ceil(students_count * 0.9)
    second_exam = math.ceil(first_exam * 0.9)
    continuing = math.ceil(second_exam * 0.8)
    if season_count % 3 == 0:
        prezapisali = math.ceil(continuing * 0.15)
    else:
        prezapisali = math.ceil(continuing * 0.05)
    continuing += prezapisali
    students_count = continuing
print(f'Students: {students_count}')



