N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(3001)]

dp[0][0] = 1

MOD = 998244353 

sum_arr = [0] * (N + 1)

sum_arr[0] = 1

for i in range(3001):
    for j in range(1,N+1):
        if a[j-1] <= i <= b[j-1]:
            dp[i][j] += sum_arr[j-1] % MOD
            sum_arr[j] += dp[i][j]
        
ans = 0      
for i in range(3001):
    ans += dp[i][N] % MOD

print(ans % MOD)