N,M = map(int,input().split())
A = list(map(int,input().split()))
BIG = 10 ** 18
dp = [[-BIG for i in range(M+1)] for j in range(N+1)]
# dp[i][j]: i番目までの要素から、j個の要素からなる部分列を選択するときの最大値
dp[0][0] = 0
for i in range(N):
    for j in range(M):
        if j <= (i+1):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
        if (j+1) <= (i+1):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+(j+1)*A[i])


print(max([d[-1] for d in dp]))


