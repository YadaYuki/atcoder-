N = int(input())
L_max = -1
BIG = 10 ** 9 + 1
R_min = BIG
ans = []
for _ in range(N):
    L, R = map(int, input().split())
    L_max = max(L_max, L)
    R_min = min(R_min, R)
    if L_max <= R_min:
        ans.append(0)
    else:
        ans.append(-(-(L_max - R_min) // 2))

for i in ans:
    print(i)