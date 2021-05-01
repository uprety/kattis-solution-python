C = input()
K = input()

def shift(x):
     return  (ord(x) - 65)



def plain_letter(c, k, i):
    num_c = shift(c)
    num_k = shift(k)
    if i % 2 == 0:
        s = (num_c - num_k) % 26    
    else:
        s = (num_c + num_k) % 26

    return chr(s + 65)

S = ''
for i in range(len(C)):
    S += plain_letter(C[i], K[i], i )

print(S)

