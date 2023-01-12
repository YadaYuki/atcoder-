from collections import defaultdict
N = int(input())
coordinates_to_id = {}
xy = list()
for i in range(N):
    x,y = map(int,input().split())
    coordinates_to_id[(x,y)] = i
    xy.append((x,y))

graph = [list() for i in range(N)]
for i in range(N):
    x,y = xy[i]
    next_coordinates = [(x-1,y-1),(x-1,y),(x,y-1),(x,y+1),(x+1,y),(x+1,y+1)]
    for next_coordinate in next_coordinates:
        if next_coordinate in coordinates_to_id:
            graph[i].append(coordinates_to_id[next_coordinate])

# 
visited = [False for i in range(N)]
def dfs(prev,cur):
    for n in graph[cur]:
        if visited[n]:
            continue
        if n == prev:
            continue
        visited[n] = True
        dfs(cur,n)
ans = 0
for i in range(N):
    if not visited[i]:
        dfs(-1,i)
        ans += 1
print(ans)