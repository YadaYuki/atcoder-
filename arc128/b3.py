def cost(r,g,b):
    r,g,b = sorted([r,g,b],reverse=True)
    BIG = 10000000000
    ans = BIG
    if (r - g) % 3 == 0:
        ans = min(ans, r)
    if (r - b) % 3 == 0:
        ans = min(ans, r)
    if (g-b) % 3 == 0:
        ans = min(ans, g)
    if ans == BIG:
        ans = -1
    return ans


T = int(input())
ans = []
for _ in range(T):
    r,g,b = map(int, input().split())
    ans.append(cost(r,g,b))

for i in ans:
    print(i)
