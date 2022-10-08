from collections import defaultdict
N,K = map(int,input().split())
A = list(map(int,input().split()))

A_sum = [0]

for i in range(N):
    A_sum.append(A_sum[i] + A[i])

A_sum_dict = defaultdict(int)

ans = 0

for i in range(N+1):
    ans += A_sum_dict[A_sum[i] - K]
    A_sum_dict[A_sum[i]] += 1

print(ans)

