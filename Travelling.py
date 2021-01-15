current_savings = 0
while True:
    destination = input()
    if destination == 'End':
        break
    minimal_budget = float(input())
    while True:
        savings = float(input())
        current_savings += savings
        if current_savings >= minimal_budget:
            print(f"Going to {destination}!")
            current_savings = 0
            break
