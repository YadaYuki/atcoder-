N = int(input())
A = list(map(int, input().split()))


A_sum = [0]
for i in A:
    if not i:
        A_sum.append(A_sum[-1] - 1)
    else:
        A_sum.append(A_sum[-1] + 1)

max_A_for_i = A_sum[0]
min_A_for_i = A_sum[0]
max_score = float('-inf')
min_score = float('inf')
for i in A_sum:
    max_score = max(max_score, i - min_A_for_i)
    min_score = min(min_score, i - max_A_for_i)

    max_A_for_i = max(max_A_for_i, i)
    min_A_for_i = min(min_A_for_i, i)

print(max_score - min_score + 1)