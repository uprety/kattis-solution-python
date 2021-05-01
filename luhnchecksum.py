
def luhnchecksum(num):
    rev_num = num[::-1]
    rev_num_2x = [ 2 * int(x) if i % 2 == 1 else int(x) for i, x in enumerate(rev_num)]
    rev_num_2x_singleDigit = [ x if x < 10 else 1 + x - 10  for x in rev_num_2x]
    return "PASS" if sum(rev_num_2x_singleDigit) % 10  == 0 else "FAIL"


T = int(input())
for _ in range(T):
    print(luhnchecksum(input()))
