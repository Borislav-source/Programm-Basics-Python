hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

time =''


if hour_of_exam == hour_of_arrival and minute_of_exam == minute_of_arrival: time = 'On time'

elif hour_of_exam == hour_of_arrival:
    if minute_of_arrival > minute_of_exam: time = 'Late'
    elif (minute_of_exam - minute_of_arrival) <= 30: time = 'On time'
    else: time = 'Early'

elif hour_of_exam > hour_of_arrival:
    if hour_of_exam - hour_of_arrival <= 1 and ((60 - minute_of_arrival) + minute_of_exam ) <= 30: time = 'On time'
    else: time = 'Early'

elif hour_of_exam < hour_of_arrival: time = 'Late'

if hour_of_exam == hour_of_arrival and minute_of_exam == minute_of_arrival: print("On time")

elif hour_of_exam - hour_of_arrival >= 1 and minute_of_exam == minute_of_arrival:
    print(f'''{time}
{hour_of_exam - hour_of_arrival}:00 hours before the start''')

elif hour_of_exam == hour_of_arrival:
    if minute_of_arrival > minute_of_exam:
        print(f'''{time}
{minute_of_arrival - minute_of_exam} minutes after the start''')
    elif (minute_of_exam - minute_of_arrival ) <= 30:
        print(f'''{time}
{minute_of_exam - minute_of_arrival} minutes before the start''')
    else:
        print(f'''{time}
{minute_of_exam - minute_of_arrival} minutes before the start''')

elif hour_of_exam > hour_of_arrival:
    if hour_of_exam - hour_of_arrival > 1:
        if minute_of_exam > minute_of_arrival:
            if 60 - ((60 - minute_of_exam) + minute_of_arrival) <= 9:
                print(f'''{time}
{hour_of_exam - hour_of_arrival}:0{60 - ((60 - minute_of_exam) + minute_of_arrival)} hours before the start''')
            else:
                print(f'''{time}
{hour_of_exam - hour_of_arrival}:{60 - ((60 - minute_of_exam) + minute_of_arrival)} hours before the start''')
        elif minute_of_exam < minute_of_arrival:
            if (60 - minute_of_arrival) + minute_of_exam <= 9:
                print(f'''{time}
{hour_of_exam - hour_of_arrival - 1}:0{(60 - minute_of_arrival) + minute_of_exam} hours before the start''')
            else:
                print(f'''{time}
{hour_of_exam - hour_of_arrival - 1}:{(60 - minute_of_arrival) + minute_of_exam} hours before the start''')
        else: print(f'''{time}
{hour_of_exam - hour_of_arrival}:{(60 - minute_of_arrival) + minute_of_exam} hours before the start''')

    elif hour_of_exam - hour_of_arrival == 1 and ((60 - minute_of_arrival) + minute_of_exam ) <= 30:
        print(f'''{time}
{((60 - minute_of_arrival) + minute_of_exam )} minutes before the start''')
    else:
        print(f'''{time}
{((60 - minute_of_arrival) + minute_of_exam )} minutes before the start''')

elif hour_of_exam < hour_of_arrival:
    if hour_of_arrival - hour_of_exam == 1 and minute_of_exam > minute_of_arrival:
        print(f'''{time}
{(60 - minute_of_exam) + minute_of_arrival} minutes after the start''')

    elif minute_of_exam < minute_of_arrival:
        if abs(60 - ((60 - minute_of_exam) + minute_of_arrival)) <=9:
            print(f'''{time}
{hour_of_arrival - hour_of_exam}:0{abs(60 - ((60 - minute_of_exam) + minute_of_arrival))} hours after the start''')
        else:
            print(f'''{time}
{hour_of_arrival - hour_of_exam}:{abs(60 - ((60 - minute_of_exam) + minute_of_arrival))} hours after the start''')
    elif minute_of_exam > minute_of_arrival:
        if (60 - minute_of_exam) + minute_of_arrival <= 9:
            print(f'''{time}
{hour_of_arrival - hour_of_exam - 1}:0{(60 - minute_of_exam) + minute_of_arrival} hours after the start''')
        else:print(f'''{time}
{hour_of_arrival - hour_of_exam - 1}:{(60 - minute_of_exam) + minute_of_arrival} hours after the start''')
    elif minute_of_exam == minute_of_arrival:
        print(f'''{time}
{hour_of_arrival - hour_of_exam}:{'00'} hours after the start''')








