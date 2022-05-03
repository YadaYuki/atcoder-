
N,M,K,S,T,X = map(int,input().split())
edges = []
for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edges.append((u,v))
S-=1
T-=1
X-=1
MOD = 998244353

dp = [[[0]*2 for _ in range(N)] for _ in range(K+1)]

dp[0][S][0] = 1

for i in range(K):
    for edge in edges:
        u,v = edge
        for x in range(2):
            dp[i+1][u][x^(u==X)] += dp[i][v][x]
            dp[i+1][v][x^(v==X)] += dp[i][u][x]
            dp[i+1][u][x^(u==X)] %= MOD
            dp[i+1][v][x^(v==X)] %= MOD
print(dp[K][T][0])