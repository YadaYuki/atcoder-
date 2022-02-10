N = int(input())
A = list(map(int,input().split()))
dp = [[0 for _ in range(10)] for _ in range(N)]


for j in range(10):
    if j == A[0]:
        dp[0][j] = 1

MOD = 998244353

for i in range(1,N):
    for j in range(10):
        dp[i][(j+A[i])%10] = (dp[i-1][j] + dp[i][(j+A[i])%10]) % MOD
        dp[i][(j*A[i])%10] = (dp[i-1][j] + dp[i][(j*A[i])%10]) % MOD

for j in range(10):
    print(dp[N-1][j])