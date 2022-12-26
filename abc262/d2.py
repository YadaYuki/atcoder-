N = int(input())
A = list(map(int,input().split()))
MOD = 998244353
ans = 0
for i in range(1,N+1):
    dp = [[[0 for _ in range(i)] for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for j in range(N):
        for k in range(j + 1): # 1 ~ j vs 0 ~ j
            for l in range(i):
                # print(j,k,l)
                dp[j+1][k][l] = (dp[j+1][k][l] + dp[j][k][l]) % MOD
                dp[j+1][k+1][(l + A[j-1])%i] =  (dp[j + 1][k + 1][(l + A[j-1])%i] + dp[j][k][l]) % MOD
    
    ans = (ans + dp[N][i][0]) % MOD
    # print(dp)
print(ans)