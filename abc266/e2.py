N = int(input())
dp = [0.0 for i in range(N+1)]
dp[0] = 3.5
for i in range(1,N+1):
    for d in [1,2,3,4,5,6]:
        d = float(d)
        dp[i] += max(dp[i-1],d)
    dp[i] /= 6
print(dp[N-1])
