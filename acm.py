submission = input().strip()

submissions = []

while submission != '-1':
    submission_response = submission.split()
    submission_response[0] = int(submission_response[0])
    submissions.append(submission_response)
    submission = input().strip()

def response_check():
    total = 0
    for result in submissions:
        total += 1 if result[2] == 'right' else 0
    return total

def total_submission_time(i):
    time = 0
    for j in range(i):
        if submissions[j][1] == submissions[i][1]:
            time += 20
    return time + submissions[i][0]


def total_time_measured():
    time = 0
    for i, result in enumerate(submissions):
        if result[2] == 'right':
            time += total_submission_time(i)
    return time

print(response_check(), total_time_measured())

