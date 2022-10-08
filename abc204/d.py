N = int(input())
T = list(map(int, input().split()))
T_sum = sum(T)
dp = [[False] * (T_sum + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(T_sum + 1):
        if j + T[i] < T_sum + 1:
            dp[i+1][j + T[i]] = dp[i][j] or dp[i+1][j + T[i]]
        dp[i+1][j] = dp[i][j] or dp[i+1][j]

# print(dp[1])
for i in range(T_sum + 1):
    if dp[N][i] and i >= -(-T_sum // 2) :
        print(i)
        break
# print(dp)

