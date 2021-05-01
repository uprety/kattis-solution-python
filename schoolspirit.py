n =  int(input())

def collective_score(index = -1):
    total = 0
    c_index = 0
    for i in range(n):
        if i != index:
            total += scores[i] * (4/5) ** c_index
            c_index += 1
    return total / 5

scores = [int(input()) for _ in range(n)]

print(collective_score())

s_score = []
for i in range(n):
    s_score.append(collective_score(i))

print(sum(s_score)/n)
