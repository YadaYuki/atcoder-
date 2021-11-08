N = int(input())
X,Y = map(int,input().split())
lunch_box = [[-1,-1]] # dummy

for _ in range(N):
    A,B = map(int,input().split())
    lunch_box.append([A,B])

dp = [[[float("inf") for _ in range(301)] for _ in range(301)] for _ in range(N+1)] # (x,y,z)でz番目目でのお弁当でx,y個のたい焼きとたこ焼きを購入するときの、購入するお弁当の最小個数が入る

dp[0][0][0] = 0 # 0個のお弁当で0個のたい焼きとたこ焼きは0

for i in range(1,N+1):
    for j in range(0,301): # たこ焼き
        for k in range(0,301): # たい焼き
            dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][k])
            A,B = lunch_box[i]
            if j >= A and k >= B:
                dp[i][j][k] = min(dp[i][j][k],dp[i-1][j-A][k-B] + 1)



# X,Y以上のたい焼きとたこ焼きを購入するために買う必要のある弁当の個数
ans = float("inf")
for i in range(N+1):
    for j in range(0,301):
        for k in range(0,301):
            if X <= j and Y <= k:
                ans = min(ans,dp[i][j][k])


if ans == float("inf"):
    print(-1)
else:
    print(ans)
