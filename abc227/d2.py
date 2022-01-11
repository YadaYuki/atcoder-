

ok,ng = -1,10 ** 18

N,K = map(int,input().split())
A = list(map(int,input().split()))


def is_possible(P):
    sum = 0
    for i in range(N):
        sum += min(A[i] , P)
    return sum >= P * K

while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if is_possible(mid):
        ok = mid
    else:
        ng = mid

print(ok)
