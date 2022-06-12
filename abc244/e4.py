N,M,K,S,T,X = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(M)]
MOD = 998244353
dp = [[[0]*2 for _ in range(N+1)] for _ in range(K+1)]

dp[0][S][0] = 1

for i in range(K):
    for edge in edges:
        a,b  = edge
        for from_n,to_n in [(a,b),(b,a)]:
            if to_n == X: # Xの登場回数の偶奇が変わる
                dp[i+1][to_n][0] = (dp[i][from_n][1] + dp[i+1][to_n][0]) % MOD
                dp[i+1][to_n][1] = (dp[i][from_n][0] + dp[i+1][to_n][1]) % MOD
            else:
                dp[i+1][to_n][0] = (dp[i][from_n][0] + dp[i+1][to_n][0]) % MOD
                dp[i+1][to_n][1] = (dp[i][from_n][1] + dp[i+1][to_n][1]) % MOD

print(dp[K][T][0])
