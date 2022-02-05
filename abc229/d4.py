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
while i < len(dot_sum):
    j = i
    dot_sum_i = dot_sum[i]
    while True:
        j += 1
        if j >= len(dot_sum):
            break
        if dot_sum[j] - dot_sum_i > K:
            break
    ans = max(j-i-1, ans)
    i = j

print(ans)