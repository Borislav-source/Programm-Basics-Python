hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())
time = ''
if hour_of_exam >= hour_of_arrival:
    if hour_of_exam == hour_of_arrival and minute_of_exam == minute_of_arrival: time = 'On time'
    if hour_of_exam - hour_of_arrival >= 1 and abs((60 - minute_of_arrival) + minute_of_exam) > 30 : time = 'Early'
    if hour_of_exam - hour_of_arrival >= 2: time = 'Early'
    if hour_of_exam - hour_of_arrival == 1 and abs(minute_of_arrival - minute_of_exam) > 30 : time = 'On time'
elif hour_of_exam <= hour_of_arrival:
    if hour_of_exam < hour_of_arrival: time = 'Late'
    if hour_of_exam == hour_of_arrival and minute_of_exam < minute_of_arrival: time = 'Late'
print(time)
if hour_of_exam != hour_of_arrival or minute_of_exam != minute_of_arrival:
    if hour_of_exam - hour_of_arrival >= 1:
        if hour_of_exam - hour_of_arrival == 1 and abs((60 - minute_of_arrival) + minute_of_exam) > 30 :
            print(f'''{time}
{abs((60 - minute_of_arrival) + minute_of_exam)} minutes before the start ''')
        else: print(f'''{time}
{abs(hour_of_arrival - hour_of_exam)} : {abs(60 - (minute_of_arrival + minute_of_exam))}''')