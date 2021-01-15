import math
students_count = int(input())
problems_count = int(input())

sum = students_count * math.ceil(problems_count * 2.8) + (students_count * math.floor(problems_count / 3))

space_needed = 5 * math.ceil(sum / 10)
print(f"""{space_needed} KB needed
{sum} submissions""")