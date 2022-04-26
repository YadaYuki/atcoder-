N, K = map(int, input().split())
A = list(map(int, input().split()))
 
ng = -1
ok = 2000000000
while ok - ng > 1:
    mid = (ok + ng) // 2
    total = 0
    for a in A:
        if a > mid:
            total += a - mid
    if total <= K:
        ok = mid
    else:
        ng = mid
 
a_min = ok

ans = 0
for a in A:
    if a > a_min:
        ans += (a + a_min + 1) * (a - a_min) // 2
        K -= a - a_min 
 
if K > 0:
    ans += K * a_min
print(ans)
