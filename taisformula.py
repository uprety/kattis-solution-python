N = int(input())

def getDetail():
    return map(float, input().split())

total_area = 0

pt, pv = getDetail() 

for i in range(N-1):
    ct, cv = getDetail()
    time_diff = ct - pt
    value_tota = cv + pv
    total_area += value_tota / 2 * time_diff
    pt, pv = ct, cv

print(total_area/1000)
