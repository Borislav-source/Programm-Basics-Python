hours = int(input())
minutes = int(input())

if minutes + 15 > 59: hours = hours + 1
if minutes + 15 <= 59: minutes = minutes + 15
elif minutes +15 > 59: minutes = 15 - (60 - minutes)
if hours > 23: hours = 0

if minutes <= 9: print(f"{hours}:0{minutes}")
else:print(f"{hours}:{minutes}")
