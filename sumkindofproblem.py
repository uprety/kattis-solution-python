def sumkindofproblem(N):
    s1 = 0
    for i in range(N + 1):
        s1 += i

    c1 = -1
    s2 = 0
    for i in range(N):
        c1 += 2
        s2 += c1

    c2 = 0
    s3 = 0
    for i in range(N):
        c2 += 2
        s3 += c2

    return (map(str, ((s1, s2, s3))))

P = int(input())
for i in range(P):
    K, N = map(int, input().split())
    print(K, ' '.join(sumkindofproblem(N)))

