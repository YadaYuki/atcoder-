S = input()
chokudai = "chokudai"
dp = [[0 for _ in range(len(chokudai) + 1)] for _ in range(len(S)+1)]

for i in range(0,len(S)+1):
  dp[i][0] = 1


for i in range(1,len(S)+1):
  for j in range(1,len(chokudai)+1):
    if S[i-1] == chokudai[j-1]:
      dp[i][j] = dp[i-1][j-1] +  dp[i-1][j]
    else:
      dp[i][j] = dp[i-1][j]
print(dp[len(S)][len(chokudai)])  
  

