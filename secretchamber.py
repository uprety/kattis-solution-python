m, n = map(int, input().split())

dic = dict()

for _ in range(m):
    key, value = map(str, input().split())

    if key in dic:
        dic[key].append(value)
    else:
        dic[key] = [value]

def checkMatchLetter(o, t, checkedKeys):
    if o == t:
        return True
    
    if o in checkedKeys:
        return False
    
    checkedKeys.append(o)

    if o in dic:
        meanings = dic[o]

        for meaning in meanings:
            if checkMatchLetter(meaning, t, checkedKeys):
                return True

    return False

for _ in range(n):
    original, translated = map(str, input().split())

    if not(len(original) == len(translated)):
        print("no")
        continue

    isMatched = False
    for i in range(len(original)):
        isMatched = checkMatchLetter(original[i], translated[i], [])

        if not isMatched:
            print("no")
            break;

    if isMatched:
        print("yes")
