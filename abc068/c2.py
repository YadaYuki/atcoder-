from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N)] 

for _ in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)

Q = deque()

cost = [float("inf")] * N # 島1から島iまでの最小コスト
visited = [False] * N

Q.appendleft(0)
cost[0] = 0
visited[0] = True

while len(Q) != 0:
    cur_island = Q.pop()

    # 隣り合った島を探索

    for island_next_to in graph[cur_island]:
        if not visited[island_next_to]:
            cost[island_next_to] = min(cost[cur_island] + 1,cost[island_next_to])
            visited[island_next_to] = True
            Q.appendleft(island_next_to)


if cost[N-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

