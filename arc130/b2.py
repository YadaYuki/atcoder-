
H,W,C,Q = map(int,input().split())
query = []

for _ in range(Q):
    t,n,c = map(int,input().split())
    query.append([t,n,c])


count = [0] * (C+1)
done_h = set() # 何行目が塗られているか
done_w = set() # 何列目が塗られているか
for i in range(Q-1,-1,-1):
    t,n,c = query[i]
    if t == 1:
        if n in done_w: # すでに塗られている
            continue
        count[c] += W - len(done_h)
        done_w.add(n)
    else:
        if n in done_h: # すでに塗られている
            continue
        count[c] += H - len(done_w)
        done_h.add(n)


print(*count[1:])

