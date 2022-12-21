# C++で実装し直す。
from collections import defaultdict
N,M = map(int,input().split())
A,B,C,D,E,F = map(int,input().split())

obstructions = set([tuple(map(int,input().split())) for i in range(M)])

dp = [
    defaultdict(int) for i in range(N+1)
]
MOD= 998244353
dp[0][(0,0)] = 1
for i in range(N):
    for coordinate,path_cnt in dp[i].items():
        x,y = coordinate
        for next_coordinates in [(x+A,y+B),(x+C,y+D),(x+E,y+F)]:
            dp[i+1][next_coordinates] = (dp[i][(x,y)] + dp[i+1][next_coordinates]) % MOD

ans = 0
for coordinate,path_cnt in dp[N].items():
    ans = (ans + path_cnt) % MOD
print(ans)