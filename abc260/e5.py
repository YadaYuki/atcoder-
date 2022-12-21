N,M = map(int,input().split())
pairs = [-1 for i in range(M+1)]
A,B = list(),list()
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    pairs[a] = max(pairs[a],b)

imos = [0 for i in range(M+2)]

r = max(A)
for l in range(1,min(B)+1):
    min_length = r - l + 1
    max_length = M - l + 1

    imos[min_length] += 1
    imos[max_length+1] -= 1

    if pairs[l] > 0:
        r = max(r,pairs[l])

for i in range(1,len(imos)):
    imos[i] += imos[i-1]


print(*imos[1:M+1])