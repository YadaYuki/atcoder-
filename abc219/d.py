N = int(input())
X, Y = map(int, input().split())

dp = [[[float("inf") for _ in range(Y+1)] for _ in range(X+1)]
      for _ in range(N+1)]

AB = []

for i in range(N):
    AB.append(list(map(int, input().split())))

dp[0][0][0] = 0

for i in range(1, N+1):
    for j in range(X):
        for k in range(Y):
          A,B = AB[i-1]
          jj = min(j+A,X)
          kk = min(k+B,Y)
          dp[i][jj][kk] = min(dp[i][jj][kk],dp[i-1][j][k] + 1)
          dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][k])

ans = dp[N][X][Y]
if ans  == float("inf"):
  print(-1)
else:
  print(ans)