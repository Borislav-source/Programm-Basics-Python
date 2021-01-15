problem = int(input())
points = int(input())
course = input()
result = 0
if problem == 1:
    if course == 'Basics':
        result = points * 0.08
        result *= 0.8
    if course == 'Fundamentals':
        result = points * 0.11
    if course == 'Advanced':
        result = points * 0.14
        result *= 1.2
if problem == 2:
    if course == 'Basics':
        result = points * 0.09
    if course == 'Fundamentals':
        result = points * 0.11
    if course == 'Advanced':
        result = points * 0.14
        result *= 1.2
if problem == 3:
    if course == 'Basics':
        result = points * 0.09
    if course == 'Fundamentals':
        result = points * 0.12
    if course == 'Advanced':
        result = points * 0.15
        result *= 1.2
if problem == 4:
    if course == 'Basics':
        result = points * 0.10
    if course == 'Fundamentals':
        result = points * 0.13
    if course == 'Advanced':
        result = points * 0.16
        result *= 1.2

print(f'Total points: {result:.2f}')