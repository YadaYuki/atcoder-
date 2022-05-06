N,L,W = map(int,input().split())
a = list(map(int,input().split())) # ソート済み
covered = []

for i in a:
    covered.append([i,i+W])

covered.append([L,L]) # dummy

not_covered = []

last_not_covered_left = 0
for cover in covered:
    l,r = cover
    if last_not_covered_left < l:
        not_covered.append([last_not_covered_left,l])
    last_not_covered_left = r

ans = 0
for not_cover in not_covered:
    not_cover_range = not_cover[1] - not_cover[0]
    ans += - (-not_cover_range // W)
print(ans)