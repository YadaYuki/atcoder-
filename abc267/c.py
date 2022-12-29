N,M = map(int,input().split())
A = list(map(int,input().split()))
A_sum = [0]

for i in range(N):
    A_sum.append(A_sum[-1] + A[i])
BIG = 10 ** 18
c = 0
for i in range(M):
    c += (i+1) * A[i]
ans = -BIG
for l in range(0,N-M+1):
    ans = max(c,ans)
    r = l + M
    if l == (N-M):
        break
    c = c + M * A[r] - (A_sum[r] - A_sum[l])
print(ans)
