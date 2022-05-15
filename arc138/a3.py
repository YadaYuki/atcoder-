N,K = map(int,input().split())
A = list(map(int,input().split()))
A_idx = [[A[i],i] for i in range(N)]

A_idx.sort(key=lambda x:(x[0],-x[1]))

ans = 10**6

max_j = -1
for a_idx in A_idx:
    a,i = a_idx
    if i >= K and max_j != -1: # K番目以降の要素であった場合、それまでに登場したj(K番目以下)の中で最大のものが候補となる
        ans = min(ans,i-max_j)
    elif i < K:
        max_j = max(max_j,i) # K番目までの要素であった場合、それまでに登場したj(<K)の中で最大のものが候補となる

if ans == 10**6:
    print(-1)
else:
    print(ans)