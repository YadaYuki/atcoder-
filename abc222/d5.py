
N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
MOD = 998244353
max_b = max(b)
R = [[0 for _ in range(max_b+1)] for _ in range(N)]

# R[i][j] = 動的計画法の累積和

for j in range(max_b+1):
    if a[0] <= j <= b[0]:
        R[0][j] = (R[0][j-1] + 1) % MOD
    else:
        R[0][j] = R[0][j-1]


for i in range(1,N):
    for j in range(max_b+1):
        if a[i] <= j <= b[i]:
            R[i][j] = (R[i][j-1] + R[i-1][j]) % MOD
        else:
            R[i][j] = R[i][j-1]

print(R[N-1][max_b])