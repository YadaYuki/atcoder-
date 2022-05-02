MOD = 998244353
N,M,K,S,T,X = map(int,input().split())

graph = [[] for _ in range(N)]
edges = []
for _ in range(M):
    u,v = map(int,input().split())
    edges.append((u-1,v-1))

S-=1
T-=1
X-=1

dp = [[[0]*2 for _ in range(N)] for _ in range(K+1)]

dp[0][S][0] = 1

for i in range(K):
    for edge in edges:
        u,v = edge
        for x in range(2):
            dp[i + 1][v][x ^ (v == X)] = (dp[i + 1][v][x ^ (v == X)] + dp[i][u][x]) % MOD
            dp[i + 1][u][x ^ (u == X)] = (dp[i + 1][u][x ^ (u == X)] + dp[i][v][x]) % MOD


print(dp[K][T][0])