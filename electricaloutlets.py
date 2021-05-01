def total_outlet(power_outlet):
    return sum(power_outlet[1:]) - power_outlet[0] + 1

N = int(input())
for _ in range(N):
    power_outlet = list(map(int, input().split()))
    print(total_outlet(power_outlet))
