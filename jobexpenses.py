def getExpense(i):
    if i < 0:
        return -1*i
    return 0

N = input()
train = map(int, input().split())

print(sum(map(getExpense, train)))

