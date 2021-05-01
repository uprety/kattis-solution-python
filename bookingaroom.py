r, n = map(int, input().split())

if r == n:
    print('too late')
else:
    x = [int(input()) for _ in range(n)]
    for i in range(r+1):
        if i+1 not in x:
            print(i+1)
            break


