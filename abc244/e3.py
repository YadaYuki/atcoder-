N,M,K,S,T,X = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

dp = [[[0]*2 for _ in range(N+1)] for _ in range(K+1)]

MOD = 998244353
dp[0][S][0] = 1
for i in range(K):
    for edge in edges:
        n1,n2 = edge
        # dp[i+1][n2] += dp[i][n1]
        # dp[i+1][n1] += dp[i][n2]
        if n1 == X:
            dp[i+1][n1][0] += dp[i][n2][1]
            dp[i+1][n1][0] %= MOD
            dp[i+1][n1][1] += dp[i][n2][0]
            dp[i+1][n1][1] %= MOD
            dp[i+1][n2][0] += dp[i][n1][0]
            dp[i+1][n2][0] %= MOD
            dp[i+1][n2][1] += dp[i][n1][1]
            dp[i+1][n2][1] %= MOD
        elif n2 == X:
            dp[i+1][n2][0] += dp[i][n1][1]
            dp[i+1][n2][0] %= MOD
            dp[i+1][n2][1] += dp[i][n1][0]
            dp[i+1][n2][1] %= MOD
            dp[i+1][n1][0] += dp[i][n2][0]
            dp[i+1][n1][0] %= MOD
            dp[i+1][n1][1] += dp[i][n2][1]
            dp[i+1][n1][1] %= MOD
        else:
            dp[i+1][n1][0] += dp[i][n2][0]
            dp[i+1][n1][0] %= MOD
            dp[i+1][n1][1] += dp[i][n2][1]
            dp[i+1][n1][1] %= MOD
            dp[i+1][n2][0] += dp[i][n1][0]
            dp[i+1][n2][0] %= MOD
            dp[i+1][n2][1] += dp[i][n1][1]
            dp[i+1][n2][1] %= MOD


# print(dp)
print(dp[K][T][0])
