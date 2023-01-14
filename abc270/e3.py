N,K = map(int,input().split())
A = list(map(int,input().split()))

ng,ok = 0,K+1
while ok - ng > 1:
    mid = (ok + ng) // 2
    K_tmp = K
    for i in range(N):
        K_tmp -= min(A[i],mid)
    
    if K_tmp <= 0:
        ok = mid
    else:
        ng = mid
ok-=1
for i in range(N):
    k = min(A[i],ok)
    K -= k
    A[i] -= k
if K == 0:
    print(*A)
else:
    for i in range(N):
        if K == 0:
            break
        k = min(1,A[i])
        K -= k
        A[i] -= k
    print(*A)


