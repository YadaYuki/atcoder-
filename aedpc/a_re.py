N = int(input())
p = list(map(int, input().split()))
max_point = sum(p)

dp = [[False for _ in range(max_point+1)] for _ in range(N+1)]

# 0点は全てTrue
for i in range(N+1):
  dp[i][0] = True

# dp
for i in range(1,N+1):
  for j in range(1,max_point+1):
    cur_point = p[i-1]
    if dp[i-1][j]:
      dp[i][j] = True
    if cur_point <= j and dp[i-1][j-cur_point]:
      dp[i][j] = True

ans = 0
for i in range(max_point+1):
  ans += int(dp[N][i])

print(ans)


