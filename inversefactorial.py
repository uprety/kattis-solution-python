import math 

def smallInverseFactorial(n):
    if n == 1:
        return 1
    pre = 1
    ans = 1
    while ans != n:
        ans *= pre
        pre += 1
    return pre -1 

def largeInverseFactorial(n):
    len_n = len(n)
    i = 1
    ans = 1
    while True:
        ans += math.log10(i)
        if ans >= len_n:
            return i
        i += 1

value = input()
if len(value) < 2:
    print(smallInverseFactorial(int(value)))
else:
    print(largeInverseFactorial(value))
