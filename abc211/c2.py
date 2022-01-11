S = input()

MOD = 10**9 + 7
chokudai = 'chokudai'
dp = [[0 for _ in range(len(chokudai) + 1)] for _ in range(len(S)+1)]

# 動的計画法により解く

for i in range(len(S) + 1):
    for j in range(len(chokudai) + 1):
        if j == 0: # chokudaiが空文字の場合
            dp[i][j] = 1
        elif i == 0: # Sが空文字の場合
            dp[i][j] = 0
        elif S[i-1] == chokudai[j - 1]:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
        elif S[i-1] != chokudai[j-1]:
            dp[i][j] = dp[i-1][j]


print(dp[-1][-1])

