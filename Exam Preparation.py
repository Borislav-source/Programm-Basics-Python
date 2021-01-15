number_bad_grades = int(input())

bad_grades = 0
avr_grade = 0
grade_count = 0

while number_bad_grades > bad_grades:
    name_problem = input()
    if name_problem == 'Enough': break
    current_grade = int(input())
    grade_count += 1
    if current_grade <= 4:
        bad_grades += 1
    avr_grade += current_grade
    last_name = name_problem
avr_grade /= grade_count

if name_problem == 'Enough':
    print(f'''Average score: {avr_grade:.2f}
Number of problems: {grade_count}
Last problem: {last_name}''')
else:
    print(f'You need a break, {bad_grades} poor grades.')

