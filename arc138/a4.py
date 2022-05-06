N,K = map(int,input().split())
A = list(map(int,input().split()))
A_idx = [(A[i],i) for i in range(N)]

A_idx.sort(reverse=True,key=lambda x:(x[0],-x[1]))

BIG = 4 * 10**5 + 1
j_min = BIG
ans = BIG
for i in range(N):
    a,idx = A_idx[i]
    if idx < K:
        if j_min != BIG:
            ans = min(ans,j_min-idx)
    else:
        j_min = min(j_min,idx)

if ans == BIG:
    print(-1)
else:
    print(ans)