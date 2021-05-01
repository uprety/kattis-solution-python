def g(i, j):
    return parking_lot[i][j]

def ifParking(i, j):       # Return no. of car smashed. -1 is no parking application
    smashing = 0
    thisPoing = [g(i, j), g(i+1, j), g(i, j+1), g(i+1, j+1)] 
    if '#' in thisPoing:
        return -1

    return thisPoing.count('X')


R, C = map(int, input().split())
parking_lot  = []
for _ in range(R):
    parking_lot.append(input())

smashedPark = [0] * 5

for i in range(R-1):
    for j in range(C - 1):
        x = parking_lot[i][j]
        if x != '#':
            parking = ifParking(i, j)
            if parking != -1:
                smashedPark[parking] = smashedPark[parking] + 1

for item in smashedPark:
    print(item)
