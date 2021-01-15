temperature = float(input())
time_to_time = str(input())

if time_to_time == 'Morning':
    if temperature >= 10 and temperature <= 18\
            : print(f"It's{temperature: .0f} degrees, get your Sweatshirt and Sneakers.")
    elif temperature >= 18 and temperature <= 24\
        : print(f"It's{temperature: .0f} degrees, get your Shirt and Moccasins.")
    elif temperature >= 25\
        : print(f"It's{temperature: .0f} degrees, get your T-Shirt and Sandals.")
elif time_to_time == 'Afternoon':
    if temperature >= 10 and temperature <= 18\
            : print(f"It's{temperature: .0f} degrees, get your Shirt and Moccasins.")
    elif temperature >= 18 and temperature <= 24\
        : print(f"It's{temperature: .0f} degrees, get your T-Shirt and Sandals.")
    elif temperature >= 25\
        : print(f"It's{temperature: .0f} degrees, get your Swim Suit and Barefoot.")
elif time_to_time == 'Evening':
    if  temperature >= 10 and temperature <= 18\
            : print(f"It's{temperature: .0f} degrees, get your Shirt and Moccasins.")
    elif temperature >= 18 and temperature <= 24\
        : print(f"It's{temperature: .0f} degrees, get your Shirt and Moccasins.")
    elif temperature >= 25\
        : print(f"It's{temperature: .0f} degrees, get your Shirt and Moccasins.")