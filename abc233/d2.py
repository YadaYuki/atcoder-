from collections import defaultdict
N,K = map(int,input().split())

A = list(map(int,input().split()))

A_sum = [0]

for i in range(N):
    A_sum.append(A_sum[i]+A[i])

d = defaultdict(int)
ans = 0
for i in range(N+1):
    ans += d[A_sum[i]]
    d[A_sum[i]+K] += 1

print(ans)


