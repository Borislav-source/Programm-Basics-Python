budgt = float(input())
season = str(input())
if season == 'summer':
    if budgt <= 100: destination = 'Bulgaria'; result = budgt * 0.3; vid = 'Camp'
    elif budgt <= 1000: destination = 'Balkans'; result = budgt * 0.4; vid = 'Camp'
    elif budgt > 1000: destination = 'Europe'; result = budgt * 0.9; vid = 'Hotel'
if season == 'winter':
    if budgt <= 100: destination = 'Bulgaria'; result = budgt * 0.7; vid = 'Hotel'
    elif budgt <= 1000: destination = 'Balkans'; result = budgt * 0.8; vid = 'Hotel'
    elif budgt > 1000: destination = 'Europe'; result = budgt * 0.9; vid = 'Hotel'
print(f'''Somewhere in {destination}
{vid} -{result: .2f}''')



