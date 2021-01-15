vid_figura = str(input())
a = float(input())

import math

if vid_figura == 'square': lice = a * a
if vid_figura == 'rectangle': b = float(input()); lice = a * b
if vid_figura == 'circle': lice = (a * a) * math.pi
if vid_figura == 'triangle': b = float(input()); lice = a * (b / 2)
print(f"{lice: .3f}")