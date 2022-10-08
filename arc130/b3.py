from collections import defaultdict

H,W,C,Q = map(int,input().split())
tnc = [list(map(int,input().split())) for _ in range(Q)]
tnc.reverse()
row_filled = defaultdict(bool)
col_filled = defaultdict(bool)
ans = [0] * C

for t,n,c in tnc:
    if t == 1:
        if row_filled[n]:
            continue
        ans[c-1] += W - len(col_filled)
        row_filled[n] = True
    else:
        if col_filled[n]:
            continue
        ans[c-1] += H - len(row_filled)
        col_filled[n] = True



print(*ans)