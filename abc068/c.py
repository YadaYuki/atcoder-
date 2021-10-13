from collections import deque

N,M = map(int,input().split())

G = [[] for _ in range(N)]

for _ in range(0,M):
    ai,bi = map(int,input().split())
    G[ai-1].append(bi-1)
    G[bi-1].append(ai-1)


dist = []

for _ in range(N):
    dist.append(-1)

dist[0] = 0


q = deque()

q.append(0)
while len(q) > 0:
    i = q.popleft()

    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            q.append(j)

if dist[N-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")



