from collections import defaultdict

N = int(input())
coordinates_dict = defaultdict(bool)
coordinates = []

for _ in range(N):
    x,y = map(int, input().split())
    coordinates_dict[(x,y)] = True
    coordinates.append([x,y])

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        xi,yi = coordinates[i]
        xj,yj = coordinates[j]
        if xi == xj or yi == yj:
            continue
        xk,yk = xi,yj
        xl,yl = xj,yi
        if coordinates_dict[(xk,yk)] and coordinates_dict[(xl,yl)]:
            ans += 1
print(ans//2)