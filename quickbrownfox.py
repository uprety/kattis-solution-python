def get_pangram(phrase):
    small_alphabets = [chr(i) for i in range(97, 97+26)]

    for l in phrase:
        if l.lower() in small_alphabets:
            small_alphabets.remove(l.lower())

    if len(small_alphabets) == 0:
        return 'pangram'
    else:
        return 'missing {}'.format(''.join(small_alphabets))


N = int(input())
for _ in range(N):
    phrase = input()
    print(get_pangram(phrase))
