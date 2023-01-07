from sys import setrecursionlimit
setrecursionlimit(10**6)


def dfs(prev,cur):
    for n in graph[cur]:
        if prev == n:
            continue
        if visited[n]:
            continue
        visited[n] = True
        dfs(cur,n)
    

N,M = map(int,input().split())
graph = [[] for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)
visited = [False for i in range(N)]
ans = 0
for s in range(N):
    if not visited[s]:
        visited[s] = True
        dfs(-1,s)
        ans += 1

print(ans)





