import heapq

N,M = map(int,input().split())
graph = []

for _ in range(N):
    graph.append([])

for _ in range(M):
    u,v,c = map(int,input().split())
    graph[u].append((v,c))

Q = [] # ヒープ


dist = [-1 for _ in range(N)]
done = [False for _ in range(N)]
dist[0] = 0

heapq.heappush(Q, (dist[0],0))

while len(Q) > 0:
    d,i = heapq.heappop(Q)

    if done[i]:
        continue

    done[i] = True

    # iと隣接するノードを探索

    for (node,cost) in graph[i]:
        if dist[node] == -1 or dist[i] + cost < dist[node]:
            dist[node] = dist[i] + cost
            heapq.heappush(Q, (dist[i] + cost,node))
    

print(dist[N-1])





