from collections import defaultdict
N = int(input())
snukes = list()
TX_2_A = defaultdict(int)
T_max = -1
for i in range(N):
    t,x,a = map(int,input().split())
    snukes.append([t,x,a])
    TX_2_A[(t,x)] = max(TX_2_A[(t,x)],a)
    T_max = max(t,T_max)

BIG = 10 ** 18
dp = [[-BIG for i in range(5)] for j in range(T_max+1)]
dp[0][0] = 0
for t in range(1,T_max+1):
    for x in range(5):
        dp[t][x] = max(dp[t-1][max(0,x-1)],dp[t-1][x],dp[t-1][min(4,x+1)])
        dp[t][x] = max(dp[t][x],dp[t][x] + TX_2_A[(t,x)])

ans = max(dp[-1])
print(ans)




