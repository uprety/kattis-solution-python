N, M, K = map(int, input().split())

classes = [ False for i in range(K)]

students = [input() for _ in range(N)]
colors = 0

for i in range(M):
    allocated = False
    for j in range(N):
        if classes[ord(students[j][i]) - 65] :
            allocated = True
            color = classes[ord(students[j][i]) - 65]
            break

    if not allocated:
        colors += 1
        allocated = colors

    for j in range(N):
        classes[ord(students[j][i]) - 65] = allocated
print(colors)
