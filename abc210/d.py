BIG = 10 ** 15

H,W,C = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(H)]



cost_after_build_first_station = [[BIG for _ in range(W)] for _ in range(H)] # 一つ目の駅を建設した後に、i,jにいるとき、それまでにかかる最小コスト

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            cost_after_build_first_station[i][j] = A[i][j]
        elif i==0:
            cost_after_build_first_station[i][j] = min(A[i][j],cost_after_build_first_station[i][j-1] + C)
        elif j==0:
            cost_after_build_first_station[i][j] = min(A[i][j],cost_after_build_first_station[i-1][j] + C)
        else:
            cost_after_build_second_station[i][j] = min(A[i][j],cost_after_build_first_station[i][j-1] + C,cost_after_build_first_station[i-1][j] + C)

cost_after_build_second_station= [[BIG for _ in range(W)] for _ in range(H)] # 一つ目の駅を建設した後に、i,jにいるとき、それまでにかかる最小コスト

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            cost_after_build_second_station[i][j] = A[i][j] + cost_after_build_first_station[i][j-1] + C
        elif j==0:
            cost_after_build_second_station[i][j] = A[i][j] + cost_after_build_first_station[i-1][j] + C
        else:
            cost_after_build_second_station[i][j] = min(A[i][j] + cost_after_build_first_station[i][j-1] + C,A[i][j] + cost_after_build_first_station[i-1][j] + C)
    

ans = BIG

for i in range(H):
    for j in range(W):
        ans = min(ans,cost_after_build_second_station[i][j])


print(ans)

