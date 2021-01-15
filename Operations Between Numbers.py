n1 = int(input())
n2 = int(input())
operator = str(input())
result = 0
vid = ''
if operator == '+' or operator == '-' or '*':
    if operator == '+':
        result = n1 + n2
        if result % 2 == 0: vid = 'even'
        else: vid = 'odd'
    elif operator == '-':
        result = n1 - n2
        if result % 2 == 0: vid = 'even'
        else: vid = 'odd'
    elif operator == '*':
        result = n1 * n2
        if result % 2 == 0: vid = 'even'
        else: vid = 'odd'
if operator == '/':
    if n2 == 0:
        result = 0
    else: result = n1 / n2
if operator == '%':
    if n2 == 0:
        result = 0
    else: result = n1 % n2
if operator == '/':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} ={result: .2f}")
elif operator == '%':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {result}")
else: print(f"{n1} {operator} {n2} = {result} - {vid}")




