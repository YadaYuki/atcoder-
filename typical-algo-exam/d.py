import heapq

N, M = map(int, input().split())

G = [[] for _ in range(N)]

dist = [-1 for _ in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))

done = [False for _ in range(N)]

Q = []

heapq.heappush(Q, (0, 0))

dist[0] = 0

while len(Q) > 0:
    _,i = heapq.heappop(Q)

    if done[i]:
        continue
    
    done[i] = True

    for (v,c) in G[i]:
        if dist[v] == -1 or dist[v] > dist[i] + c:
            dist[v] = dist[i] + c
            heapq.heappush(Q,( dist[v],v))

print(dist[N-1])
