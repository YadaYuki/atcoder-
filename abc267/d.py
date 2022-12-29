N,M = map(int,input().split())
A = list(map(int,input().split()))
BIG = 10**18
dp = [[-BIG for i in range(M+1)] for j in range(N+1)]

dp[0][0] = 0

for i in range(1,N+1):
    for j in range(0,M+1):
        if j > i:
            break
        dp[i][j]=max(dp[i][j],dp[i-1][j])

        if j > 0:
            dp[i][j] = max(dp[i][j],dp[i-1][j-1]+j*A[i-1])
ans = -BIG
for i in range(N+1):
    ans = max(ans,dp[i][M])
print(ans)