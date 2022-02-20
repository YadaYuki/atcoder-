N,X = map(int,input().split())

dp = [[False]*(X+1) for _ in range(N+1)]
ab = [list(map(int,input().split())) for _ in range(N)]

dp[0][0] = True

for i in range(N+1):
    for j in range(X+1):
        a,b = ab[i-1]
        for distance in [a,b]:
            if j + distance <= X:
                dp[i][j+distance] = dp[i-1][j] or dp[i][j+distance]

# print(dp)
print("Yes" if dp[N][X] else "No")




