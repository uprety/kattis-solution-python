def playable():
    global horses
    if horses[0] + 1 == horses[1] and horses[1] + 1 == horses[2]:
        return False
    return True

def distant():
    global horses
    return 2 if horses[1] - horses[0] <= horses[2] - horses[1] else 0

def play():
    global horses
    if playable():
        return abs(horses[distant()] - horses[1]) - 1
    return 0

horses = list(map(int, input().split()))
if __name__ == '__main__':
    print(abs(play()))

