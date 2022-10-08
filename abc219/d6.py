N = int(input())
X,Y = map(int,input().split())

BIG = 301
dp = [[[BIG for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]

dp[0][0][0] = 0

AB = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N+1):
    a,b = AB[i-1]
    for j in range(X+1):
        for k in range(Y+1):
            dp[i][min(X,j+a)][min(Y,k+b)] = min(dp[i][min(X,j+a)][min(Y,k+b)],dp[i-1][j][k] + 1)
            dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][k])

if dp[N][X][Y] == BIG:
    print(-1)
else:
    print(dp[N][X][Y])

# print()
