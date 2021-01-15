income = float(input())
sreden_uspeh = float(input())
minimal_wage = float(input())
import math
scholarship = math.floor(minimal_wage * 0.35)
scholarship2 = math.floor(sreden_uspeh * 25)


if income < minimal_wage and sreden_uspeh > 4.5 and sreden_uspeh < 5.5:
    print(f"You get a Social scholarship {scholarship: .0f} BGN")
elif income > minimal_wage and sreden_uspeh >= 5.5:
    print(f"You get a scholarship for excellent results{scholarship2: .0f} BGN")
elif sreden_uspeh >= 5.5 and income < minimal_wage:
    if scholarship > scholarship2: print(f"You get a Social scholarship{scholarship: .0f} BGN")
    elif scholarship2 >= scholarship: print(f"You get a scholarship for excellent results{scholarship2: .0f} BGN")
else:
    print("You cannot get a scholarship!")
