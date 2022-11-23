N,M = map(int,input().split())
graph = [[] for _ in range(N)] 

for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    graph[v].append(u)
    graph[u].append(v)
ans = 0
for a in range(N):
    for b in graph[a]:
        for c in graph[b]:
            if a in graph[c]:
                ans += 1
                # print(a,b,c)

print(ans//6)