import math
students_count = int(input())
problems_count = int(input())
energy = int(input())
cicles = 0
questions_count = 0
while True:
    if students_count < 10 or energy <= 0:
        break
    energy += problems_count * 2
    students_count -= problems_count
    energy -= (students_count * 2) * 3
    questions_count += (students_count * 2)
    cicles += 1
    students_count += math.floor(students_count / 10)
total = cicles * problems_count

if energy <= 0:
    print(f'''The trainer is too tired!
Questions asked: {questions_count}''')
elif students_count < 10:
    print(f'''The students are too few!
Problems solved: {total}''')