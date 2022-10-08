from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

A_to_cnt = defaultdict(int)

for a in A:
    A_to_cnt[a] += 1


ans = N * (N-1) * (N-2) // 6


for a in A_to_cnt:
    if A_to_cnt[a] >= 2:
        ans -= ((A_to_cnt[a] * (A_to_cnt[a] - 1)) // 2) * (N - A_to_cnt[a])
    if A_to_cnt[a] >= 3:
        ans -= (A_to_cnt[a] * (A_to_cnt[a] - 1) * (A_to_cnt[a] - 2)) // 6

print(ans)