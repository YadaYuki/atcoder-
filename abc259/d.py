from collections import deque
N = int(input())
sx,sy,tx,ty = map(int,input().split())
circles = [
    list(map(int,input().split())) for _ in range(N)
]


graph = [[] for _ in range(N)]

for i in  range(N-1):
    for j in range(i+1,N):
        ci,cj = circles[i],circles[j]
        xi,yi,ri = ci
        xj,yj,rj = cj
        d = (xi-xj)**2 + (yi-yj) ** 2
        if (ri - rj) ** 2 <= d <= (ri+rj) ** 2:
            graph[i].append(j)
            graph[j].append(i)

start = -1
end = -1
for i in range(N):
    xi,yi,ri = circles[i]
    if (sx - xi) ** 2 + (sy-yi) ** 2 == ri ** 2:
        start = i
    if (tx - xi) ** 2 + (ty-yi) ** 2 == ri ** 2:
        end = i

# BFS

q = deque([start])
visited = [False for _ in range(N)]
visited[start] = True

while len(q)>0 and not visited[end]:
    cur = q.popleft()
    for n in graph[cur]:
        if not visited[n]:
            q.append(n)
            visited[n] = True
            if visited[end]:
                break


if visited[end]:
    print("Yes")
else:
    print("No")