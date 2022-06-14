import heapq

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
indegrees = [0]*N
for _ in range(M):
    A,B = map(int,input().split())
    graph[A-1].append(B-1)
    indegrees[B-1] += 1

heap = []
for i in range(N):
    if indegrees[i] == 0:
        heapq.heappush(heap, i)
visited = [False]*N
ans = []
while len(heap) > 0:
    node = heapq.heappop(heap)
    visited[node] = True
    ans.append(node+1)
    for i in graph[node]:
        indegrees[i] -= 1
        if indegrees[i] == 0:
            heapq.heappush(heap, i)


if len(ans) == N:
    print(*ans)
else:
    print(-1)