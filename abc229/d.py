S = input()
K = int(input())

dot_num = [0]

for i in range(len(S)):
    if S[i] == "X":
        dot_num.append(dot_num[i])
    else:
        dot_num.append(dot_num[i] + 1)

r = 0
ans = 0
for i in range(len(S)):
    while dot_num[r] - dot_num[i] <= K:
        if r >= len(S):
            break
        r += 1
    ans = max(ans,r - i)

print(ans)
