def countWhiteRegions(circles):
    print(circles)
    return 'Done' # Number of white region

dataSet = int(input())

while dataSet != 0:
    circles  =  list(map(int, input().split()))

    while len(circles) != 3 * dataSet:
        circles += list(map(int, input().split()))

    print(countWhiteRegions(circles))
    dataSet = int(input())
