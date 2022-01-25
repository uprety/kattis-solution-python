from math import log10, floor

#memo = {}
#def getFactorial(n):
#    global memo
#    if n == 1:
#        return 1
#    elif n in memo:
#        return memo[n]
#    else:
#        result = n * getFactorial(n -1 )
#        memo[n] = result
#        return result

def smallInverseFactorial(n):
    pre = 1
    ans = 1
    while ans != n:
        ans *= pre
        pre += 1
    return pre -1 

def largeInverseFactorial(n):
    len_n = len(str(n))
    i = 1
    ans = 1
    while True:
        ans += log10(i)
        if floor(ans) == len_n:
            return i
        i += 1

value = input()

if len(value) < 3:
    value =  int(value)
    if value == 1:
        print(1)
    else:
        print(smallInverseFactorial(value))
else:
    print(largeInverseFactorial(value))
