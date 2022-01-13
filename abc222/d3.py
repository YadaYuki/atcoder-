N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

M = max(b)
MOD =  998244353
pattern_num  = [[0] * (M+1) for _ in range(N+1)] # pattern_num[i][j] = c[i]=jの時のi番目までの場合の数
pattern_num_sum = [[0] * (M+1) for _ in range(N+1)]
pattern_num[0][0] = 1
pattern_num_sum[0][0] = 1
for i in range(N+1):
    for j in range(M+1):
        if i == 0 and j == 0:
            pattern_num[i][j] = 1
            pattern_num_sum[i][j] = 1
        elif a[i-1] <= j <= b[i-1]:
            pattern_num[i][j] = pattern_num_sum[i-1][j]
            pattern_num_sum[i][j] = (pattern_num_sum[i-1][j] + pattern_num_sum[i][j-1]) % MOD
        else:
            pattern_num[i][j] = 0
            pattern_num_sum[i][j] = pattern_num_sum[i][j-1]

# 長さNの場合の数を全て足す.
print(pattern_num_sum[N][M])




