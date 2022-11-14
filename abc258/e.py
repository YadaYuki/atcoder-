N,Q,X = map(int,input().split())
W = list(map(int,input().split()))

query = []
for _ in range(Q):
    query.append(int(input()))
SumWgt = sum(W)
Ncnt = 0
while X > SumWgt:
    Ncnt += N * (X//SumWgt)
    X %= SumWgt 
Arrow = [-1] * N
PotatoCnt = [0] * N
s,r = 0,0
for l in range(N):
    if l > 0:
        s -= W[l-1]
    
    while s < X:
        s += W[r%N]
        r += 1

    Arrow[l] = r%N
    PotatoCnt[l] = r-l
    
x = 0
idx = 1
Seen = [-1] * N
Rec = []

while idx :
    if Seen[x] < 0:
        Seen[x] = idx
        Rec.append(x)
        idx += 1
    else:
        PreCyc = Seen[x]
        Cycle = idx - PreCyc
        break

    x = Arrow[x]
    
ans = []
for k in query:
    if k - PreCyc > 0:
        k = (k - PreCyc) % Cycle + PreCyc
    
    a = PotatoCnt[Rec[k-1]] + Ncnt
    ans.append(a)

print(*ans, sep="\n")
