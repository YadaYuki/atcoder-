N,X = map(int,input().split())
A,B = list(),list()
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

dp = [[False for i in range(X+1)] for j in range(N+1)]
dp[0][0] = True
for i in range(N):
    ai,bi = A[i],B[i]
    for j in range(X+1):
        dp[i+1][j] = dp[i][j] or dp[i+1][j]
        for b in range(1,bi+1):
            if j+ai*b > X:
                break
            dp[i+1][j+ai*b] = dp[i][j] or dp[i+1][j+ai*b]

if dp[N][X]:
    print("Yes")
else:
    print("No")


