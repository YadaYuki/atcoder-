import sys
from bisect import bisect_left

N,M = map(int,input().split())
AB = []
for _ in range(M):
    a,b = map(int,input().split())
    AB.append([a,b])

AB.sort(key=lambda x:(x[0],-x[1]))

# Aは昇順、Bは降順

INF = 1 << 30

dp = [INF] * (N+1)

for a,b in AB:
    i = bisect_left(dp, b)
    dp[i] = b

print(bisect_left(dp, INF))