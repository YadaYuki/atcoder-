N = int(input())
a = list(map(int,input().split()))
MOD = 998244353
ans = 0
for i in range(1,N+1):
    dp = [[[0]*(i) for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for j in range(N):
        for k in range(j+1):
            for l in range(i):
                # j + 1項目を使う.
                dp[j+1][k][l] = (dp[j][k][l] + dp[j+1][k][l]) % MOD
                dp[j+1][k+1][(l+a[j])%i] = (dp[j][k][l] + dp[j+1][k+1][(l+a[j])%i]) % MOD

    ans = (ans + dp[N][i][0]) % MOD

print(ans)