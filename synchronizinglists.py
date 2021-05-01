def getlist(n):
    return [int(input()) for _ in range(n)]

def get_index_value(l):
    sorted_l = sorted(l)
    indexes= []
    for num in l:
        indexes.append(sorted_l.index(num))
    return indexes

def arrange_l2():
    index_l1 = get_index_value(l1)
    index_l2 = get_index_value(l2)
    arranged_l2  = []
    for i in range(len(l1)):
        l2_value = l2[i]
        if index_l1[i] != index_l2[i]:
            l2_value = l2[index_l2.index(index_l1[i])]
        arranged_l2.append(l2_value) 
    return arranged_l2


n = int(input())
while n:
    l1 = getlist(n)
    l2 = getlist(n)
    for num in arrange_l2():
        print(num)
    n = int(input())
    if n:
        print()

