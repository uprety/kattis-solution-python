gunnar = (map(int, input().split()))

emma = (map(int, input().split()))

sum_g = sum(gunnar)
sum_e = sum(emma)

if sum_g == sum_e:
    print('Tie')
elif sum_g > sum_e:
    print('Gunnar')
else:
    print('Emma')
