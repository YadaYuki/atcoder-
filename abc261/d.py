N,M = map(int,input().split())
X = list(map(int,input().split()))
bonus = [0 for _ in range(N+1)]

for i in range(M):
    c,y = map(int,input().split())
    bonus[c] = y

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(i+1):
        # head
        dp[i+1][j+1] = max(dp[i][j] + bonus[j+1] + X[i],dp[i+1][j+1])
        # tail
        dp[i+1][0] = max(dp[i][j],dp[i+1][0])

# print(dp)
print(max(dp[N]))
