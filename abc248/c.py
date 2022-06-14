MOD = 998244353
N,M,K = map(int,input().split())
dp = [[0] * N*M for _ in range(N)]

for i in range(M):
    dp[0][i] = 1


for i in range(1,N):
    for j in range(1,N*M):
        k = max(0,j-M)
        for l in range(k,j):
            dp[i][j] += dp[i-1][l]
            dp[i][j] %= MOD
ans = 0
for i in range(K):
    ans += dp[N-1][i]
    ans %= MOD


print(ans)