H,W,C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


BIG = 10**10
cost_after_build_first_station = [[BIG for _ in range(W)] for _ in range(H)]

ans = BIG

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            cost_after_build_first_station[i][j] = A[i][j]
        elif i == 0:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i][j-1] + C)
            ans = min(ans, cost_after_build_first_station[i][j-1] + C + A[i][j])
        elif j == 0:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i-1][j] + C)
            ans = min(ans, cost_after_build_first_station[i-1][j] + C + A[i][j])
        else:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i-1][j] + C, cost_after_build_first_station[i][j-1] + C)
            ans = min(ans, cost_after_build_first_station[i-1][j] + C + A[i][j], cost_after_build_first_station[i][j-1] + C + A[i][j])


for i in range(H):
    for j in range(W-1,-1,-1):
        if i == 0 and j == W-1:
            cost_after_build_first_station[i][j] = A[i][j]
        elif i == 0:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i][j+1] + C)
            ans = min(ans, cost_after_build_first_station[i][j+1] + C + A[i][j])
        elif j == W-1:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i-1][j] + C)
            ans = min(ans, cost_after_build_first_station[i-1][j] + C + A[i][j])
        else:
            cost_after_build_first_station[i][j] = min(A[i][j], cost_after_build_first_station[i-1][j] + C, cost_after_build_first_station[i][j+1] + C)
            ans = min(ans, cost_after_build_first_station[i-1][j] + C + A[i][j], cost_after_build_first_station[i][j+1] + C + A[i][j])

print(ans)