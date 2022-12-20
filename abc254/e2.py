from collections import deque
N,M = map(int,input().split())
graph = [[] for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)


Q = int(input())
ans_ls = []
for i in range(Q):
    x,k = map(int,input().split())
    x -= 1
    # BFS
    cost_to_vertices = {}
    cost_to_vertices[x] = 0
    queue = deque([x])

    while len(queue) > 0:
        cur = queue.popleft()
        if cost_to_vertices[cur] == k:
            continue
        
        for n in graph[cur]:
            if not (n in cost_to_vertices):
                cost_to_vertices[n] = cost_to_vertices[cur] + 1
                queue.append(n)
    ans = 0
    for k,v in cost_to_vertices.items():
        ans += (k+1)
    ans_ls.append(ans) 

for a in ans_ls:
    print(a)