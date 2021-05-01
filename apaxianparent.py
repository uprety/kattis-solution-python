def name(Y, P):
    if Y[-1] == 'e':
        return Y + 'x' + P
    elif Y[-1] in ['a', 'i', 'o', 'u']:
        return Y[:-1] + 'ex' + P
    elif Y[-2:] == 'ex':
        return Y + P
    return Y + 'ex' + P

[Y, P] = input().strip().split()  
print(name(Y, P))

