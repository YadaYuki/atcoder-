N,M = map(int,input().split())

BIG = 10**9

cost = [[BIG for _ in range(N)] for _ in range(N)]

for _ in range(M):
    A,B,C = map(int,input().split())
    cost[A-1][B-1] = C

for i in range(N):
    cost[i][i] = 0

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])
            if cost[i][j] != BIG:
                ans += cost[i][j]

print(ans)