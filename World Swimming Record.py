world_record = float(input())
distance = float(input())
time_for_1_meter = float(input())
import math
delay = math.floor((distance / 15) )* 12.5

time_for_Ivancho = (distance * time_for_1_meter) + delay

result = abs(world_record - time_for_Ivancho)

if world_record > time_for_Ivancho: print(f"Yes, he succeeded! The new world record is{time_for_Ivancho: .2f} seconds.")
else:print(f'No, he failed! He was{result: .2f} seconds slower.')







