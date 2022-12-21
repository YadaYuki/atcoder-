N = int(input())
dp = [0 for i in range(N)]

dp[0] = 3.5

for i in range(1,N):
    dices = [1,2,3,4,5,6]
    for d in dices:
        dp[i] += max(dp[i-1],d) / 6

print(dp[N-1])