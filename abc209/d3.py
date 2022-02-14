from collections import deque

N,Q = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)



cost_to_node = [0]*N

queue = deque([0])
while len(queue) > 0:
    town = queue.popleft()
    for next_town in graph[town]:
        if cost_to_node[next_town] == 0:
            cost_to_node[next_town] = cost_to_node[town] + 1
            queue.append(next_town)

ans = []
for i in range(Q):
    c,d = map(int,input().split())
    if cost_to_node[c-1] % 2 == cost_to_node[d-1] % 2:
        ans.append('Town')
    else:
        ans.append('Road')

for i in range(Q):
    print(ans[i])