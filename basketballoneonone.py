def check_end():
    if step == 1:
        if playerAscore >= 11:
            return 'A'
        elif playerBscore >= 11:
            return 'B'
    elif playerAscore  > playerBscore + 1:
        return 'A'
    elif playerBscore > playerAscore + 1:
        return 'B'
    return False

player = []
score = []
playerAscore = 0
playerBscore = 0
step = 1

scores = input().strip()

for i in range(len(scores)):
    if i % 2:
        score.append(int(scores[i]))
    else:
        player.append(scores[i])


for i in range(len(player)):
    if player[i] == 'A':
        playerAscore += score[i]
        if check_end():
            break
    else:
        playerBscore += score[i]
        if check_end():
            break

    if playerAscore == 10 and playerBscore == 10:
        step = 2

print(check_end())
