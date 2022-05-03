from math import ceil
N,L,W = map(int,input().split())
a = list(map(int,input().split()))

# 覆われている区間を列挙する

covered = []

for i in a:
    covered.append([i,i+W])
covered.append([L,L]) # dummy
not_covered = []
left = 0

for cover in covered:
    if cover[0] > left:
        not_covered.append([left,cover[0]])
    left = cover[1]
ans = 0

for not_cover in not_covered:
    ans += - (-(not_cover[1] - not_cover[0]) // W)
print(ans)