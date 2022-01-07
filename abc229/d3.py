S = list(input())
K = int(input())

dot_count = [0]

for i in range(len(S)):
    if S[i] == '.':
        dot_count.append(dot_count[i] + 1)
    else:
        dot_count.append(dot_count[i])
ans = -1
j = 0
for i in range(len(dot_count)):
    while j < len(dot_count) and dot_count[j] - dot_count[i] <= K:
        j += 1
    ans = max(ans, j - i - 1)

print(ans)

