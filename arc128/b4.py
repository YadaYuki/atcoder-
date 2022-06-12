def cnt(r,g,b):
    r,g,b = sorted([r,g,b],reverse=True)
    BIG = 10 ** 18
    ans = BIG
    if (r - g) % 3 == 0:
        ans = min(ans,r)
    if (g-b) % 3 == 0:
        ans = min(ans,g)
    if (r-b) % 3 == 0:
        ans = min(ans,r)
    if ans == BIG:
        return -1
    return ans



T = int(input())
for _ in range(T):
    r,g,b = map(int,input().split())
    print(cnt(r,g,b))