from bisect import bisect_left
from collections import defaultdict

H,W,rs,cs = map(int,input().split())

N = int(input())
walls_in_cols = defaultdict(list)
walls_in_rows = defaultdict(list)

for i in range(N):
    r,c = map(int,input().split())
    walls_in_cols[c].append(r)
    walls_in_rows[r].append(c)

for k in walls_in_cols.keys():
    walls_in_cols[k].sort()

for k in walls_in_rows.keys():
    walls_in_rows[k].sort()
ans = list()
Q = int(input())
rc,cc = rs,cs
for i in range(Q):
    d,l = input().split()
    l = int(l)
    if d == "L":
        # cc より小さい
        nearest_wall_col_idx_in_left = bisect_left(walls_in_rows[rc],cc)
        if nearest_wall_col_idx_in_left == 0: # no walls in left
            wall = 0
        else:
            wall_col_in_left = walls_in_rows[rc][nearest_wall_col_idx_in_left-1]
            wall = wall_col_in_left
        cc = max(wall+1,cc-l)
    
    if d == "R":
        # cc より大きい
        nearest_wall_col_idx_in_right = bisect_left(walls_in_rows[rc],cc)
        if nearest_wall_col_idx_in_right == len(walls_in_rows[rc]): # no walls in left
            wall = W+1
        else:
            wall_col_in_right = walls_in_rows[rc][nearest_wall_col_idx_in_right]
            wall = wall_col_in_right
        cc = min(wall-1,cc+l)
    
    if d == "U":
        # rc より大きい
        nearest_wall_row_idx_in_up = bisect_left(walls_in_cols[cc],rc)
        if nearest_wall_row_idx_in_up == 0: # no walls in left
            wall = 0
        else:
            wall_col_in_up = walls_in_cols[cc][nearest_wall_row_idx_in_up-1]
            wall = wall_col_in_up
        rc = max(wall+1,rc-l)

    if d == "D":
        # rc より大きい
        nearest_wall_row_idx_in_down = bisect_left(walls_in_cols[cc],rc)
        if nearest_wall_row_idx_in_down == len(walls_in_cols[cc]): # no walls in left
            wall = H+1
        else:
            wall_col_in_up = walls_in_cols[cc][nearest_wall_row_idx_in_down]
            wall = wall_col_in_up
        rc = min(wall-1,rc+l)
    
    ans.append((rc,cc))

for a in ans:
    print(*a)

