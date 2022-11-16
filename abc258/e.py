N,Q,X = map(int,input().split())
W = list(map(int,input().split()))

query = []
for _ in range(Q):
    query.append(int(input()))
SumWgt = sum(W)

N_base = N * (X//SumWgt) # Xがジャガイモ全ての重量の合計を超えるとき、N_base個のジャガイモが必ず入る
X %= SumWgt 

# 尺取り法でarrowとPo
arrow = [-1] * N
PotatoCnt = [0] * N
cur_w,r = 0,0
for l in range(N):
    if l > 0:
        cur_w -= W[l-1]
    
    while cur_w < X:
        cur_w += W[r%N]
        r += 1

    arrow[l] = r%N
    PotatoCnt[l] = r-l

# ?
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

    x = arrow[x]

# 
ans = []
for k in query:
    if k - PreCyc > 0:
        k = (k - PreCyc) % Cycle + PreCyc
    
    a = PotatoCnt[Rec[k-1]] + N_base
    ans.append(a)

print(*ans, sep="\n")
