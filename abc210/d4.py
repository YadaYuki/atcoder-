H,W,C = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

BIG = 10**10
# 一つ目の駅を建設した後、(i,j)にいる時、の最小コスト
cost_after_build_first_station = [[BIG for _ in range(W)] for _ in range(H)] 

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            cost_after_build_first_station[i][j] = A[i][j]
        elif i == 0:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i][j-1] + C)
        elif j == 0:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i-1][j] + C)
        else:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i-1][j] + C, cost_after_build_first_station[i][j-1] + C)



# 一つ目の駅を建設した後、(i,j)にいる時、の最小コスト
cost_after_build_second_station = [[BIG for _ in range(W)] for _ in range(H)] 

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            cost_after_build_second_station[i][j] = A[i][j] + cost_after_build_first_station[i][j-1] + C
        elif j == 0:
            cost_after_build_second_station[i][j] = A[i][j] + cost_after_build_first_station[i-1][j] + C
        else:
            cost_after_build_second_station[i][j] = A[i][j] + min( cost_after_build_first_station[i-1][j], cost_after_build_first_station[i][j-1] ) + C



ans = BIG
for i in range(H):
    for j in range(W):
        ans = min(ans, cost_after_build_second_station[i][j])


cost_after_build_first_station = [[BIG for _ in range(W)] for _ in range(H)] 

for i in range(H):
    for j in range(W-1,-1,-1):
        if i == 0 and j == W-1:
            cost_after_build_first_station[i][j] = A[i][j]
        elif i == 0:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i][j+1] + C)
        elif j == W-1:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i-1][j] + C)
        else:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i-1][j] + C, cost_after_build_first_station[i][j+1] + C)



# 一つ目の駅を建設した後、(i,j)にいる時、の最小コスト
cost_after_build_second_station = [[BIG for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W-1,-1,-1):
        if i == 0 and j == W-1:
            continue
        elif i == 0:
            cost_after_build_second_station[i][j] = A[i][j] + cost_after_build_first_station[i][j+1] + C
        elif j == W-1:
            cost_after_build_second_station[i][j] = A[i][j] + cost_after_build_first_station[i-1][j] + C
        else:
            cost_after_build_second_station[i][j] = A[i][j] + min( cost_after_build_first_station[i-1][j], cost_after_build_first_station[i][j+1] ) + C

for i in range(H):
    for j in range(W):
        ans = min(ans, cost_after_build_second_station[i][j])

print(ans)