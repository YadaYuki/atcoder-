import heapq

N,M = map(int,input().split())
G = [[] for _ in range(N)]
indegrees = [0]* N
for _ in range(M):
    A,B = map(int,input().split())
    G[A-1].append(B-1)
    indegrees[B-1] += 1

zero_indegrees_nodes = []
for i in range(N):
    if indegrees[i] == 0:
        heapq.heappush(zero_indegrees_nodes,i)

P = []
while len(zero_indegrees_nodes) > 0:
    zero_indegrees_node = heapq.heappop(zero_indegrees_nodes)
    P.append(zero_indegrees_node+1)
    for node in G[zero_indegrees_node]:
        indegrees[node] -= 1
        if indegrees[node] == 0:
            heapq.heappush(zero_indegrees_nodes,node)


if len(P) == N:
    print(*P)
else:
    print(-1)


