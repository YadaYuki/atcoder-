S = [list(input()) for i in range(10)]

A,B,C,D = None,None,None,None
for i in range(10):
    if "#" in S[i]:
        A = i + 1
        b = i
        for b in range(i,10):
            if not "#" in S[b]:
                B = b
                break
        if B is None:
            B = 10
        break

sa = S[A-1]
for i in range(10):
    if sa[i] == "#":
        C = i + 1
        d = i
        for d in range(i,10):
            if not ("#" == sa[d]):
                D = d
                break
        if D is None:
            D = 10 
        break
print(A,B)
print(C,D)