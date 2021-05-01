from math import pi
d = 60
roundDistance = pi * d
pointLength = roundDistance / 28
eachTime = pointLength / 15

def getTraveledDistance(aphorism):
    aphorism = aphorism.replace(' ', chr(65+26))
    aphorism = aphorism.replace("'", chr(65+27))
    aphorismInt = [ord(x) - 64 for x in aphorism]

    currentDis = 0
    currentPos = aphorismInt[0]
    for item in aphorismInt[1:]:
        shortest  = abs(item - currentPos) 
        linearlongest = 28 - shortest
        currentDis += min(shortest, linearlongest)
        currentPos = item

    return (currentDis * eachTime) + len(aphorismInt)

for i in range(int(input())):
    print(getTraveledDistance(input()))
