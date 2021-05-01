
def ifPinkRose(button):
    required_color = ['pink', 'rose']
    for i in range(len(required_color)):
        if required_color[i] in button.lower():
            return True
    return False

N = int(input())

count_button = 0
for i in range(N):
    button = input()
    if ifPinkRose(button):
        count_button += 1

if count_button == 0:
    print('I must watch Star Wars with my daughter')
else:
    print(count_button)
