N,S = map(int,input().split())
a,b = list(),list()
sum_max = 0
for i in range(N):
    ai,bi = map(int,input().split())
    a.append(ai)
    b.append(bi)
    sum_max += max(ai,bi)

if S > sum_max:
    print("No")
    exit()

dp = [[False for i in range(sum_max + 1)] for j in range(N+1)]

dp[0][0] = True
for i in range(N):
    for j in range(sum_max):
        # 裏
        ai,bi = a[i],b[i]
        if not ((j + ai) > sum_max):
            dp[i+1][j+ai] = dp[i][j] or dp[i+1][j+ai]
        if not ((j + bi) > sum_max):
            dp[i+1][j+bi] = dp[i][j] or dp[i+1][j+bi]

if not dp[N][S]:
    print("No")
    exit()
cards = list()
cur_sum = S
for i in range(N,0,-1):
    ai,bi = a[i-1],b[i-1]
    if dp[i-1][cur_sum-ai]:
        cur_sum -= ai
        cards.append("H")
    elif dp[i-1][cur_sum-bi]:
        cur_sum -= bi
        cards.append("T")
    else:
        assert False

cards.reverse()
print("Yes")
print("".join(cards))