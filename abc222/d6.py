N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_b = max(b)
R = [[0] * (max_b + 1) for _ in range(N + 1)]


MOD = 998244353

for i in range(1,max_b+1):
    if a[0] <= i <= b[0]:
        R[0][i] = R[0][i-1] + 1
    else:
        R[0][i] = R[0][i-1]

# print(R)
for i in range(1,N):
    for c in range(max_b+1):
        if a[i] <= c <= b[i]:
            R[i][c] = (R[i][c-1] + R[i-1][c]) % MOD
        else:
            R[i][c] = R[i][c-1]

print(R[N-1][max_b])
