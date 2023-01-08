N = int(input())
dp = [0.0 for i in range(N+1)]
dices = [1,2,3,4,5,6]
for i in range(1,N+1):
    for d in dices:
        dp[i] += max(d,dp[i-1])
    dp[i] /= len(dices)
print(dp[N])
