def toDecimal(language, number):
    decimal = 0

    for i, num in enumerate(number):
        power = len(number) - i - 1
        decimal += language.find(num) * len(language) ** power

    return decimal


def toTarget(language, decimal):
    value = ""

    length  = len(language)

    while decimal >= length:
        value += language[decimal % length]
        decimal = decimal // length
    
    value += language[decimal % length]

    return value[::-1]


T = int(input())

for i in range(T):
    alien_number, source_language, target_language = input().split()

    decimal = toDecimal(source_language, alien_number)

    print("Case #{}: {}".format(
        i+1,
        toTarget(target_language, decimal)
        ))
