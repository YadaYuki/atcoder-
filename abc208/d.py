N,M = map(int,input().split())

BIG = 10**9
graph = [[BIG for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for i in range(M):
    A,B,C = map(int,input().split())
    graph[A-1][B-1] = C



ans = 0

for k in range(N):
    for j in range(N):
        for i in range(N):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            if graph[i][j] != BIG:
                ans += graph[i][j]

print(ans)