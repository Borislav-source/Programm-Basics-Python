time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third
import math
minutes = math.floor(total_time / 60)
seconds = total_time % 60


if seconds <= 9: print(f"{minutes}:0{seconds}")
else: print(f"{minutes}:{seconds}")
