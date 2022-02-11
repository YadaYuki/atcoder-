N = int(input())
X,Y = map(int,input().split())
lunch_boxes = [list(map(int,input().split())) for _ in range(N)]
BIG = 1000000000
dp = [[[BIG for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]


dp[0][0][0] = 0

# 配るDPで解く
for i in range(N):
    A,B = lunch_boxes[i]
    for j in range(X+1):
        for k in range(Y+1):
            jj = min(j+A,X)
            kk = min(k+B,Y)
            dp[i+1][jj][kk] = min(dp[i+1][jj][kk],dp[i][j][k]+1)
            dp[i+1][j][k] = min(dp[i+1][j][k],dp[i][j][k])

ans = dp[N][X][Y]
if ans == BIG:
    print(-1)
else:
    print(ans)
