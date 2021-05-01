n =  int(input())

stored_value = [input() for _ in range(n)]

for i in range(n-1, -1, -1):
    print(stored_value[i])

