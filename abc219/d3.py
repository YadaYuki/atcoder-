N = int(input())
X,Y = map(int,input().split())
A = []
B = []
sum_taiyaki,sum_takoyaki = 0,0
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

INF = 10 ** 10 # 購入する弁当の数が300を超えることはない

dp = [[[INF for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
ans = INF

dp[0][0][0] = 0 # 弁当がひとつもない状態の時、たい焼き・たこ焼きが0個になる弁当の数は0
for i in range(N+1):
    for j in range(X+1):
        for k in range(Y+1):
            jj = min(j+A[i-1],X)
            kk = min(k+B[i-1],Y)
            dp[i][jj][kk] = min(dp[i][jj][kk],dp[i-1][j][k] + 1)
            dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][k])
                
ans = dp[N][X][Y]

if ans == INF:
    print(-1)
else:
    print(ans)