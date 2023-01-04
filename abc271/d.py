N,S = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(N)]
dp = [[False for j in range(10001)] for i in range(N+1)]


dp[0][0] = True
# 配るDP

for i in range(N):
    ai,bi = ab[i]
    for j in range(10001):
        if j + ai <= 10000:
            dp[i+1][j+ai] = dp[i+1][j+ai] or dp[i][j]
        if j + bi <= 10000:
            dp[i+1][j+bi] = dp[i+1][j+bi] or dp[i][j]
if dp[-1][S]:
    print("Yes")
    ans = list()
    s = S
    for i in range(N-1,-1,-1):
        # H(a)
        ai,bi = ab[i]
        if dp[i][s-ai]:
            s -= ai
            ans.append("H")
        # T(b)
        elif dp[i][s-bi]:
            s -= bi
            ans.append("T")
    ans.reverse()
    print("".join(ans))

else:
    print("No")

