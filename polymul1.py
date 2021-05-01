def polyMul(poly1, poly2):
    polyResult = [0]*(len(poly1) + len(poly2) - 1 )

    for index1, item1 in enumerate(poly1):
        for index2, item2 in enumerate(poly2):
            index = index1 + index2
            result = item1 * item2
            polyResult[index] += result



    print(len(polyResult) - 1 )
    print(" ".join([ str(x) for x in polyResult]))

if __name__ == '__main__':
    T = int(input())
    for K in range(T):
        U =  input()
        poly1 = list(map(int, input().split()))
        V =  input()
        poly2 = list(map(int, input().split()))
        polyMul(poly1, poly2)
