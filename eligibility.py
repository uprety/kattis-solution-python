def getYear(date):
    return int(date[:4])


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        name, startedYear, DoB, courses = input().split()
        startedYear, birthYear = map(getYear, [startedYear, DoB])
        if startedYear >= 2010 or birthYear >= 1991:
            print(name, 'eligible')
        elif int(courses) >=  41:
            print(name, 'ineligible')
        else:
            print(name, 'coach petitions')
