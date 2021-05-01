def mul(a):
    total = 1
    for i in a:
        total *= i
    return total

print( mul(map(int, input().split())))
