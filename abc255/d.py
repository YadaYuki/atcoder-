N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
A_sum = [A[0]]
for i in range(1,N):
    A_sum.append(A_sum[-1] + A[i])


for i in range(Q):
    x = int(input())
    ok,ng = -1,N
    while ng-ok > 1:
        mid = (ng + ok) // 2
        if x < A[mid]:
            ok = mid 
        else:
            ng = mid
    ans = ((ok + 1) * x - A_sum[ok]) + ((N-ok)*x - (A_sum[N-1] - A_sum[ok]))
    print(ans)