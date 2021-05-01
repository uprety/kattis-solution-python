D, S = map(int, input().split())

am = [ list(map(int, input().split())) for _ in range(D) ]
sen = [ list(map(int, input().split())) for _ in range(S) ]

for ami, amI in enumerate(am):
    con  = True
    for seni, senI in enumerate(sen):
        if amI[0] in range(senI[0], senI[1]) and con:
            print(senI[-1])
            con = False
    if con:
        print(0)
        
        

