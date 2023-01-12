S = [list(input()) for i in range(10)]
A,B,C,D = None,None,None,None
for i in range(10):
    if "#" in S[i]:
        A = i + 1
        ii = i
        while (ii < len(S)) and ("#" in S[ii]):
            ii += 1
        B = ii
        C = S[i].index("#")
        ii = C
        C += 1
        while (ii < len(S[i])) and ("#" == S[i][ii]):
            ii += 1
        D = ii
        print(A,B)
        print(C,D)
        exit()
