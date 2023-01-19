from bisect import bisect_left
from collections import defaultdict

H,W,rs,cs = map(int,input().split())
N = int(input())
walls_in_rows,walls_in_cols = defaultdict(list),defaultdict(list)

for i in range(N):
    r,c = map(int,input().split())
    walls_in_rows[r].append(c)
    walls_in_cols[c].append(r)

for k in walls_in_cols.keys():
    walls_in_cols[k].sort()

for k in walls_in_rows.keys():
    walls_in_rows[k].sort()

rc,cc = rs,cs
Q = int(input())
for i in range(Q):
    d,l = input().split()
    l = int(l)
    nearest_wall = None
    if d == "L":
        nearest_wall_idx_in_left = bisect_left(walls_in_rows[rc],cc) - 1
        if nearest_wall_idx_in_left == -1:
            nearest_wall = 0
        else:
            nearest_wall = walls_in_rows[rc][nearest_wall_idx_in_left]
        cc = max(nearest_wall+1,cc-l)

    if d == "U":
        nearest_wall_idx_in_up = bisect_left(walls_in_cols[cc],rc) - 1
        if nearest_wall_idx_in_up == -1:
            nearest_wall = 0
        else:
            nearest_wall = walls_in_cols[cc][nearest_wall_idx_in_up]
        rc = max(nearest_wall+1,rc-l)
    
    if d == "R":
        nearest_wall_idx_in_right = bisect_left(walls_in_rows[rc],cc)
        if nearest_wall_idx_in_right == len(walls_in_rows[rc]):
            nearest_wall = W + 1
        else:
            nearest_wall = walls_in_rows[rc][nearest_wall_idx_in_right]
        cc = min(nearest_wall-1,cc+l)
    
    if d == "D":
        nearest_wall_idx_in_down = bisect_left(walls_in_cols[cc],rc)
        if nearest_wall_idx_in_down == len(walls_in_cols[cc]):
            nearest_wall = H + 1
        else:
            nearest_wall = walls_in_cols[cc][nearest_wall_idx_in_down]
        rc = min(nearest_wall-1,rc+l)
    
    print(rc,cc)