N = int(input())
T = list(map(int, input().split()))
T_sum = sum(T)
dp = [[False for _ in range(T_sum+1)] for _ in range(N+1)]
dp[0][0] = True
for i in range(1,N+1):
    for j in range(T_sum+1):
        dp[i][j] = dp[i][j] or dp[i-1][j]
        if j >= T[i-1]:
            dp[i][j] = dp[i][j] or dp[i-1][j-T[i-1]]
# print(dp)

for j in range(T_sum+1):
    if dp[N][j] and j >= (T_sum//2 + T_sum%2):
        print(j)
        exit()

