W = int(input())
N = int(input())

total_area = 0
for _ in range(N):
    w, i = map(int, input().split())
    total_area += w * i

print(int(total_area/W))

