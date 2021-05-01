
def get_score(answer_sheet):
    correct_answer = 0
    for i in range(len(answer_sheet) - 1):
        if answer_sheet[i] == answer_sheet[i +1]:
            correct_answer += 1
    return correct_answer

if __name__ == '__main__':
    n = int(input())
    answer_sheet = [input() for _ in range(n)]
    print(get_score(answer_sheet))

