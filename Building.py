floor = int(input())
room = int(input())

for i in range(floor, 0, -1):
    for k in range(0, room):
        if i == floor:
            print("L{0}{1} ".format(i,k),end="")

        elif i % 2 != 0:
            print("A{0}{1} ".format(i,k),end="")

        elif i % 2 == 0:
            print("O{0}{1} ".format(i, k), end="")
    print("")