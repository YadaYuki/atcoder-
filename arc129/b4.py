N = int(input())
L_max = -1
R_min = 10**9 + 1
LR  = [list(map(int, input().split())) for _ in range(N)]
ans = []
for L,R in LR:
    L_max = max(L_max, L)
    R_min = min(R_min, R)
    lr = max(L_max-R_min, 0)
    ans.append(-(-lr // 2))

for i in ans:
    print(i)