def loop_rope(s1, s2):
    l = min(len(s1), len(s2))

    total_length = 0
    knot = 0
    for i in range(l):
        if i > 0:
            knot += 1
        total_length += s1[i]
        knot += 1
        total_length += s2[i]

    #if len(s1) > l:
    #    knot += 1
    #    total_length += s1[-1]
    knot += 1

    return total_length - knot 


def get_length(segments):

    if len(segments) == 1:
        return '0'

    red_segment = sorted([int(x[:-1]) for x in segments if x.endswith('R')], reverse=True)
    blue_segment = sorted([int(x[:-1]) for x in segments if x.endswith('B')], reverse=True)

    return max(loop_rope(red_segment, blue_segment),  loop_rope(blue_segment, red_segment))


no_of_cases = int(input())
for case in range(no_of_cases):
    no_of_segments = int(input())
    segments = input().split()
    print('Case #{}: {}'.format(case + 1, get_length(segments)))

