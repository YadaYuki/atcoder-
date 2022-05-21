from collections import defaultdict
import math

N = int(input())
A = list(map(int,input().split()))
cnt = defaultdict(int)
for a in A:
    cnt[a] += 1

ans = math.comb(N,3)

for a in cnt:
    ans -= math.comb(cnt[a],2) * (N-cnt[a])
    ans -= math.comb(cnt[a],3)
print(ans)