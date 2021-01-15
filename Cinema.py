vid_projekciq = str(input())
broi_redove = int(input())
broi_coloni = int(input())

broi_mesta = broi_coloni * broi_redove

if vid_projekciq == 'Premiere': prihod = broi_mesta * 12
elif vid_projekciq == 'Normal': prihod = broi_mesta * 7.5
elif vid_projekciq == 'Discount': prihod = broi_mesta * 5

print(f'{prihod: .2f} leva')