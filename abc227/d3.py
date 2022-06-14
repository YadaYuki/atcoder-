N,K = map(int,input().split())
A = list(map(int,input().split()))
A_s = sorted(A,reverse=True)

ok,ng = -1,10 ** 18

while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    is_possible = True
    p_num = 0
    for a in A:
        p_num += min(a,mid)
    
    if mid * K > p_num:
        is_possible = False
        
    if is_possible:
        ok = mid
    else:
        ng = mid


print(ok)
