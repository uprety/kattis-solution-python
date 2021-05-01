
def lowestDolls():
    __ = input()
    dolls = list(map(int, input().split()))
    dolls = [(dolls[i], dolls[i+1]) for i in range(0, len(dolls), 2)]
    return dolls

    
if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        print(lowestDolls())
