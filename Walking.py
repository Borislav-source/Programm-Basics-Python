goal = 10000
steps_count = 0
stps = input()
while steps_count < goal and stps != 'Going home':
    stps = int(stps)
    steps_count += stps
    if steps_count >= goal: break
    stps = input()
if stps == 'Going home':
    steps_to_home = int(input())
    difference = goal - (steps_count + steps_to_home)
    if (steps_count + steps_to_home) >= goal:
        print(f'''Goal reached! Good job!
        {abs(difference)} steps over the goal!''')
    else:
        print(f"{abs(difference)} more steps to reach goal.")
else:
    difference = steps_count - goal
    print(f'''Goal reached! Good job!
            {abs(difference)} steps over the goal!''')
    