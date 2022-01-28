S = input()
K = int(input())
dot_num = [0]

for i in range(len(S)):
    if S[i] == "X":
        dot_num.append(dot_num[i])
    else:
        dot_num.append(dot_num[i] + 1)

ans = 0
r = 0
print(dot_num)
for l in range(len(S)):
    while r < len(S) and dot_num[r+1] - dot_num[l] <= K:
        r += 1
    ans = max(ans,r - l)
    print(ans)

print(ans)