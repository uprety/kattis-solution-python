N = int(input())

players = [input() for _ in range(N)]
if sorted(players) == players:
    print("INCREASING")
elif sorted(players, reverse=True) == players:
    print("DECREASING")
else:
    print("NEITHER")
