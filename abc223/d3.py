import heapq

N,M = map(int,input().split())
G = [[] for _ in range(N)]
indegrees = [0]*N # 各ノードへの入次数
for _ in range(M):
    A,B = map(int,input().split())
    G[A-1].append(B-1)
    indegrees[B-1] += 1


heap = []

for node in range(N):
    if indegrees[node] == 0:
        heapq.heappush(heap,node)
ans = []
while len(heap) > 0:
    node = heapq.heappop(heap)
    ans.append(node+1)
    for next_node in G[node]:
        indegrees[next_node] -= 1
        if indegrees[next_node] == 0:
            heapq.heappush(heap,next_node)

if len(ans) == N:
    print(*ans)
else:
    print(-1)

