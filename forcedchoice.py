N, P, S = map(int, input().split())

for _ in range(S):
    cards = list(map(int, input().split()))
    if P in cards[1:]:
        print('KEEP')
    else:
        print('REMOVE')
