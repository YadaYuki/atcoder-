H,W,C = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(H)]

costs_after_buiid_first_station = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        costs_after_buiid_first_station[i][j] = A[i][j]
        if i > 0:
            costs_after_buiid_first_station[i][j] = min(costs_after_buiid_first_station[i-1][j]+C,costs_after_buiid_first_station[i][j])
        if j > 0:
            costs_after_buiid_first_station[i][j] = min(costs_after_buiid_first_station[i][j-1]+C,costs_after_buiid_first_station[i][j])

BIG = 10**15
ans = BIG
for i in range(H):
    for j in range(W):
        if i > 0:
            ans = min(costs_after_buiid_first_station[i-1][j]+C+A[i][j],ans)
        if j > 0:
            ans = min(costs_after_buiid_first_station[i][j-1]+C+A[i][j],ans)

for i in range(H):
    for j in range(W-1,-1,-1):
        costs_after_buiid_first_station[i][j] = A[i][j]
        if i > 0:
            costs_after_buiid_first_station[i][j] = min(costs_after_buiid_first_station[i-1][j]+C,costs_after_buiid_first_station[i][j])
        if j < W-1:
            costs_after_buiid_first_station[i][j] = min(costs_after_buiid_first_station[i][j+1]+C,costs_after_buiid_first_station[i][j])

for i in range(H):
    for j in range(W-1,-1,-1):
        if i > 0:
            ans = min(costs_after_buiid_first_station[i-1][j]+C+A[i][j],ans)
        if j < W-1:
            ans = min(costs_after_buiid_first_station[i][j+1]+C+A[i][j],ans)



print(ans)