N = int(input())
M = 3000
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mod = 998244353

# dp = []
# for _ in range(N+1):
#     dp.append([0] * (M + 1))

# dp[0][0] = 1

dp = [1] * (M+1)
# for i in range(1,N+1):
#     for j in range(M+1):
#         if A[i]
#             dp[i][j]

for i in range(N):
    nx = [0] * (M + 1)
    for j in range(A[i],B[i] + 1):
        nx[j] = dp[j]
    dp = nx
    for i in range(M):
        dp[i+1] += dp[i]
        dp[i+1] %= mod

print(dp[M])


