from collections import defaultdict
# 動的計画法
N = int(input())
snukes = defaultdict(int)
max_t = -1
for i in range(N):
    t,x,a = map(int,input().split())
    snukes[(t,x)] = a
    max_t = max(max_t,t)

# dp
BIG = 10**19
dp = [[-BIG for i in range(5)] for j in range(max_t+1)]
dp[0][0] = 0

for t in range(max_t):
    for coordinate in range(5):
        nexts = [(t+1,coordinate-1),(t+1,coordinate),(t+1,coordinate+1)]
        for n in nexts:
            nt,nc = n
            if 0 <= nc <= 4:
                dp[nt][nc] = max(dp[nt][nc],dp[t][coordinate] + snukes[(nt,nc)])

print(max(dp[-1]))

