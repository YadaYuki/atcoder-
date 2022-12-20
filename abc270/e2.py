N,K = map(int,input().split())
A = list(map(int,input().split()))


ok,ng = K+1,0

# K個以下
while ok - ng > 1:
    mid = (ok + ng) // 2

    k = K
    for a in A:
        k -= min(a,mid)
    if k <= 0:
        ok = mid
    else:
        ng = mid

m = ok - 1
for i,a in enumerate(A):
    A[i] -= min(a,m)
    K -= min(a,m)
if K == 0:
    print(*A)
    exit()
for i,a in enumerate(A):
    if a > 0:
        A[i] -= 1
        K -= 1
    if K == 0:
        print(*A)
        exit()






