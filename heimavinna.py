questions_list = input().split(';')

total_questions = 0

for q in questions_list:
    if '-' in q:
        lower, upper = map(int, q.split('-'))
        total_questions += upper - lower + 1
    else:
        total_questions += 1

print(total_questions)
