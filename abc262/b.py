N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
ans = 0
for a in range(N):
    for b in graph[a]:
        if a < b:
            for c in graph[b]:
                if b < c:
                    # print(a,b,c)
                    # print(graph[c])
                    if a in graph[c]:
                        ans += 1

print(ans)

