from collections import defaultdict,deque

N =int(input())
graph = defaultdict(list)

for  i in range(N):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited = defaultdict(bool)
visited[1] = True

while len(queue) > 0:
    cur = queue.popleft()
    for n in graph[cur]:
        if not visited[n]:
            queue.append(n)
            visited[n] = True

ans = -1
for k,v in visited.items():
    ans = max(k,ans)
print(ans)