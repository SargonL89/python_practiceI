rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

internal1 = ["x" for r in range(20)]
# print("Internal1:", internal1)

internal2 = [internal1 for f in range(15)]
# print("Internal2:", internal2)

# for row in range(5):
    # print(internal2)

mapa = [['~' for _ in range(10)] for _ in range(10)]
for i in mapa:
    print(mapa[0][5], end="")