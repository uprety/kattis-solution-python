def prod(inttlist):
    result = 1
    for intiger in intlist:
        if intiger != '0':
            result *= int(intiger)

    return result

x = input()
value = int(x)

while value >= 10:
    intlist = [z for z in x]
    value = prod(intlist)
    x = str(value)
print(value)

