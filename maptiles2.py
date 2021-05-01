quadkey = input().strip()

def getCordinate(quadkey):
    #TODO: Do something please here
    level = len(quadkey)
    x, y = 0, 0
    for i, q in enumerate(quadkey):
        x, y  = x*2, y*2
        if q == '1':
            x += 1
        elif q == '2':
            y += 1
        elif q == '3':
            x += 1
            y += 1

    print(level, x, y)
getCordinate(quadkey)
