N,K = map(int,input().split())
A = list(map(int,input().split()))
ok,ng = N,-1

while abs(ok-ng) > 1:
    mid = (ok + ng) // 2
    if A[mid]>=K:
        ok = mid
    else:
        ng = mid

if ok == N:
    print(-1)
    exit(0)
print(ok)
