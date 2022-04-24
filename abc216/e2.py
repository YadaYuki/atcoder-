N, K = map(int, input().split())
A = list(map(int, input().split()))
 
lb = -1
ub = 2000000000
while ub - lb > 1:
    mid = (ub + lb) // 2
    tot = 0
    for a in A:
        if a > mid:
            tot += a - mid
    if tot <= K:
        ub = mid
    else:
        lb = mid
 
a_min = ub
 
ans = 0
for a in A:
    if a > a_min:
        ans += (a + a_min + 1) * (a - a_min) // 2
        K -= a - a_min 
 
if K > 0:
    ans += K * a_min
print(ans)
