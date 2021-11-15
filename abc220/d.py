N = int(input())
A = list(map(int, input().split()))

dp = [[0 for i in range(10)] for _ in range(N)]

dp[0][A[0]] = 1

MOD = 998244353

for i in range(0,N-1):
    for j in range(10):
        dp[i+1][(j+A[i+1])%10] += dp[i][j] % MOD
        dp[i+1][(j*A[i+1])%10] += dp[i][j] % MOD

for i in range(10):
    print(dp[N-1][i] % MOD)
