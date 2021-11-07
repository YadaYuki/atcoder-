N = int(input())
A = list(map(int, input().split()))

dp = [[i for i in range(10)] for _ in range(N+1)]

dp[1][A[1]] = 1

for i in range(1,N):
    for j in range(10):
        dp[i+1][(j+A[i])%10] += dp[i][j]
        dp[i+1][(j*A[i])%10] += dp[i][j]

for i in range(10):
    print(dp[N][i])
