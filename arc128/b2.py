
T = int(input())
BIG = 10000000000
a = []
for _ in range(T):
    RGB = list(map(int, input().split()))
    RGB.sort(reverse=True)
    ans = BIG
    r,g,b = RGB
    if (r - g) % 3 == 0:
        cost_to_b = g + ((r - g) // 3 * 3)
        ans = min(ans, cost_to_b)
    if (r - b) % 3 == 0:
        cost_to_g = b + ((r - b) // 3 * 3)
        ans = min(ans, cost_to_g)
    if (g-b) % 3 == 0:
        cost_to_r = b + ((g - b) // 3 * 3)
        ans = min(ans, cost_to_r)
    if ans == BIG:
        ans = -1

    a.append(ans)

for i in a:
    print(i)