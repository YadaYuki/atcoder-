N,K,D = map(int,input().split())
A = list(map(int,input().split()))

dp = [[[-1 for k in range(D)] for j in range(N+1)] for i in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(N):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            dp[i+1][j+1][(dp[i][j][k]+A[i])%D] = max(dp[i+1][j+1][(dp[i][j][k]+A[i])%D], dp[i][j][k]+A[i])
            dp[i+1][j][k] = max(dp[i+1][j][k],dp[i][j][k])

print(dp[N][K][0])
