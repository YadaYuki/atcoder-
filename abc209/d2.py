from collections import deque
N,Q = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

RED,BLUE = 0,1
colors = [-1] * N

colors[0] = RED
queue = deque([0])

while len(queue) > 0:
    town = queue.popleft()
    for next_town in graph[town]:
        if colors[next_town] == -1:
            colors[next_town] = 1 - colors[town]
            queue.append(next_town)



query = []

ans = []
for _ in range(Q):
    c,d = map(int, input().split())
    if colors[c-1] != colors[d-1]:
        ans.append('Road')
    else:
        ans.append('Town')
    
for i in ans:
    print(i)