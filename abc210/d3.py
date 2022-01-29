H,W,C = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(H)]

BIG = 10**13
cost_after_build_first_station = [[BIG for _ in range(W)] for _ in range(H)] # 最初の駅を建設した後,(i,j)にいる時,それまでに生じたコスト

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            cost_after_build_first_station[i][j] = A[i][j]
        elif i == 0:
            cost_after_build_first_station[i][j] = min(A[i][j],cost_after_build_first_station[i][j-1]+C)
        elif j == 0:
            cost_after_build_first_station[i][j] = min(A[i][j],cost_after_build_first_station[i-1][j]+C)
        else:
            cost_after_build_first_station[i][j] = min(A[i][j],cost_after_build_first_station[i-1][j]+C,cost_after_build_first_station[i][j-1]+C)
        

cost_after_build_second_station = [[BIG for _ in range(W)] for _ in range(H)] # 2つ目の駅を(i,j)に建設した時,それまでに生じたコスト.


for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            cost_after_build_second_station[i][j] = A[i][j] + cost_after_build_first_station[i][j-1] + C
        elif j == 0:
            cost_after_build_second_station[i][j] = min(A[i][j],cost_after_build_first_station[i-1][j]+C)
        else:
            cost_after_build_second_station[i][j] = min(A[i][j],cost_after_build_first_station[i-1][j]+C,cost_after_build_first_station[i][j-1]+C)
