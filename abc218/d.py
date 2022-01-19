from collections import defaultdict
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
pos_map = defaultdict(bool)

for i in range(N):
    x,y = xy[i]
    pos_map[(x,y)] = True

ans = 0

for i in range(N-1):
    for j in range(i+1,N):
        xi,yi = xy[i]
        xj,yj = xy[j]
        if xi != xj and yi != yj:
            if (xi,yj) in pos_map and (xj,yi) in pos_map:
                ans += 1
print(ans//2)