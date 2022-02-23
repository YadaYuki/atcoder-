import heapq 
N,M = map(int,input().split())

graph = [[] for _ in range(N)]
indegrees = [0] * N
for _ in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    indegrees[b-1] += 1

indegree_zero_nodes=[]

for i in range(N):
    if indegrees[i] == 0:
        heapq.heappush(indegree_zero_nodes,i)

ans = []

while len(indegree_zero_nodes) > 0:
    node = heapq.heappop(indegree_zero_nodes)
    ans.append(node)
    for i in graph[node]:
        indegrees[i] -= 1
        if indegrees[i] == 0:
            heapq.heappush(indegree_zero_nodes,i)


if len(ans) == N:
    ans = [i+1 for i in ans]
    print(*ans)
else:
    print(-1)