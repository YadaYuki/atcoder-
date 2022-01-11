N,K = map(int,input().split())
A = list(map(int,input().split()))

ok,ng = 0,10 ** 18
while abs(ng-ok) > 1:# ng > okになることってあるか？ .. ない.ng > okスタートで、okはngとokの間にある値しかなる可能性がないから。
    mid = (ok + ng) // 2
    workers = 0
    for i in range(N):
        workers += min(A[i],mid) # mid = P個のプロジェクト
    if workers >= mid * K:
        ok = mid
    else:
        ng = mid

print(ok)


