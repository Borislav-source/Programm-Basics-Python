income = float(input())
sreden_uspeh = float(input())
minimal_wage = float(input())
import math
scholarship = math.floor(minimal_wage * 0.35)
scholarship2 = math.floor(sreden_uspeh * 25)
if income <= minimal_wage:
    moje = 1
else:
    moje = 2
if sreden_uspeh > 4.5:
    boje = 1
else:
    boje = 2

if sreden_uspeh >= 5.5 and moje == 1 and scholarship > scholarship2:
    print(f"You get a Social scholarship{scholarship: .0f} BGN")
elif moje == 1 and boje == 1 and sreden_uspeh < 5.5:
    print(f"You get a Social scholarship{scholarship: .0f} BGN")
elif sreden_uspeh >= 5.5 and moje == 1 and scholarship2 >= scholarship:
    print(f"You get a scholarship for excellent results{scholarship2: .0f} BGN")
elif sreden_uspeh >= 5.5 and moje == 2:
    print(f"You get a scholarship for excellent results{scholarship2: .0f} BGN")
else:
    print("You cannot get a scholarship!")
