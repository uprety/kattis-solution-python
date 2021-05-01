N = int(input())

if N % 2 == 1:
    print("still running")
else:
    stopWatchTime = 0
    stopWatchState = False
    for _ in range(N):
        current = int(input())
        if stopWatchState:
            stopWatchTime += current - previous
            stopWatchState = False
        else:
            stopWatchState = True
        previous = current
    print(stopWatchTime)
