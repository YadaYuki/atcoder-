from itertools import permutations


T = int(input())

BIG = 10000000000
perm = list(permutations(range(0, 3)))
a =[]
for _ in range(T):
    r,g,b = sorted(list(map(int, input().split())),reverse=True)
    ans = BIG 
    if (r - g) % 3 == 0:
        ans = min(ans, r)
    if (r - b) % 3 == 0:
        ans = min(ans, r)
    if (g - b) % 3 == 0:
        ans = min(ans, g)
    if ans == BIG:
        ans = -1
    a.append(ans)

for i in a:
    print(i)