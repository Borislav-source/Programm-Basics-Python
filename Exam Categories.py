complicity = int(input())
zavurtqnost = int(input())
pages_count = int(input())
if complicity >= 80 and zavurtqnost >= 80 and pages_count >= 8:
    print('Legacy')
elif complicity >= 80 and zavurtqnost <= 10:
    print('Master')
elif complicity <= 10:
    print('Elementary')
elif complicity <= 30 and pages_count <= 1:
    print('Easy')
elif zavurtqnost >= 50 and pages_count >= 2:
    print('Hard')
else:
    print('Regular')