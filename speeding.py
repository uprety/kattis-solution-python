n = int(input())

pre_t, pre_d = 0, 0
_ = input()

previous_hi_speed = 0
for _ in range(n -1):
    t, d = map(int, input().split())
    current_speed = int((d - pre_d)/(t - pre_t))
    high_speed = max(current_speed, previous_hi_speed)
    pre_t, pre_d = t, d
    previous_hi_speed = high_speed

print(high_speed)
