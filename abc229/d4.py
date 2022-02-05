S = list(input())
K = int(input())
dot_sum = [0]

for i in range(len(S)):
    if S[i] == '.':
        dot_sum.append(dot_sum[i] + 1)
    else:
        dot_sum.append(dot_sum[i])


i = 0
ans = -1
for i in range(len(dot_sum)):
    while j < len(dot_sum) and dot_sum[j] - dot_sum[i] <= K:
        j += 1
    ans = max(j-i-1, ans)

print(ans)