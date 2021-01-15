name = input()
password = input()
password2 = input()
while True:
    if password != password2:
        password2 = input()
    else:break
print(f'Welcome {name}!')

