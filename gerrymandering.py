import math

def wasted_vote(x, y):
    
    abs_majority  = math.floor((x + y) / 2) + 1
    
    if x > y:
        wasted =  x - abs_majority 
        total_wasted_vote[0] += wasted
        total_wasted_vote[1] += y
        print('A', wasted, sum_b)
    else:
        wasted =  y - abs_majority 
        total_wasted_vote[0] += x
        total_wasted_vote[1] += wasted
        print('B', sum_a, wasted)

    
def efficiency_gap():
    diff = abs(total_wasted_vote[0] - total_wasted_vote[1])

    return  diff / total_vote_casted


districts = {}
total_wasted_vote = [0, 0]
total_vote_casted = 0

P, D = map(int, input().split())

for i in range(P):
    d, A, B = map(int, input().split())
    total_vote_casted += A + B
    if d in districts:
        districts[d] = districts[d] + [A, B]
    else:
        districts[d] = [A, B]


districts = dict(sorted(districts.items(), key = lambda t: t[0]))


for key, value in districts.items():
    total_a = [ value[x] for x in range(len(value)) if x % 2 == 0]
    total_b = [ value[x] for x in range(len(value)) if x % 2 != 0]

    sum_a, sum_b = map(sum, [total_a, total_b])

    wasted_vote(sum_a, sum_b)


print(efficiency_gap())
