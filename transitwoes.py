
# For every bus, calculate the waiting time
def bus_waiting_time(time_passed, interval):
    if time_passed % interval == 0:
        return 0

    ans = interval - (time_passed % interval)
    return ans

# Reseave di, bi, ci
def getInput():
    return list(map(int, input().split()))

s, t, n = map(int, input().split())

di = getInput()
bi = getInput()
ci = getInput()

target_time = t - s

time_passed = di[0]

for i in range(n):
    time_passed += bus_waiting_time(time_passed, ci[i])
    time_passed += bi[i]
    time_passed += di[i + 1]


print('yes' if time_passed <= target_time else 'no')

