mis_spelled = input()
word_length = int(len(mis_spelled)/3)

mis_spelled_list = [[mis_spelled[y * word_length + l] for y in [0, 1, 2]] for l in range(word_length)]

correct_word = ''
for letters in mis_spelled_list:
    correct_word += max(letters, key=letters.count)

print(correct_word)
