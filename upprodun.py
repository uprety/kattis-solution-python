N = int(input())
M = int(input())

if N >= M:
    for i in range(M):
        print("*")
else:
    mod = int(M/N)
    floor_plan = [0]*N
    for i in range(N):
        floor_plan[i] += mod
    for i in range(M - N * mod):
        floor_plan[i] += 1
    for item in floor_plan:
        print("*"*item)
