observations = int(input())

m = 0
s = 0

for obs in range(observations):
    M, S = map(int, input().split())

    m += M
    s += S

averageDiffTime = (s / 60) / m
if averageDiffTime > 1:
    print(averageDiffTime)
else:
    print("measurement error")
