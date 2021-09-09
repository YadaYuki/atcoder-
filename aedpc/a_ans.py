N = int(input())
p = [0] + list(map(int, input().split()))
max_point = sum(p)

dp = [[False for _ in range(max_point+1)] for _ in range(N+1)]

dp[0][0] = True

# dp
for i in range(1,N+1):
  for j in range(max_point+1):
    if dp[i-1][j]:
      dp[i][j] = True
    if j >= p[i] and dp[i-1][j-p[i]]:
      dp[i][j] = True
    
ans = 0
for i in range(max_point+1):
  ans += int(dp[N][i])

print(ans)