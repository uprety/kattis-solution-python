def required_candel(d):
    return int(d*(d+1)/2 + d) 

for i in range(int(input())):
    n, d = map(int, input().split())

    print(n, required_candel(d))

