N = int(input())
X,Y = map(int,input().split())

lunch_boxes = []

for _ in range(N):
    A,B = map(int,input().split())
    lunch_boxes.append([A,B])

INF = 10000 # float "inf"は使わない。メモリをすごい食うみたいだ...。
dp = [ [ [ INF for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1) ]


dp[0][0][0] = 0 # 弁当がひとつもない状態の時、たい焼き・たこ焼きが0個になる弁当の数は0

for i in range(1,N+1):
    A,B = lunch_boxes[i-1]
    for j in range(X+1):
        for k in range(Y+1):
            xx = min(j+A,X)
            yy = min(k+B,Y)
            dp[i][xx][yy] = min(dp[i][xx][yy],dp[i-1][j][k] + 1)
            dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][k])

ans = dp[N][X][Y]

if ans == INF:
    print(-1)
else:
    print(ans)

