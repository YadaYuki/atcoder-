import sys
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
graph = [[] for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)



for i in range(N):
    if len(graph[i]) > 2:
        print('No')
        exit()

def dfs(prev,cur):
    visited[cur] = True
    for i in graph[cur]:
        if prev != i:
            if visited[i]:
                return True
            else:
                return dfs(cur,i)
    return False

visited = [False]*N

for i in range(N):
    if not visited[i]:
        if dfs(-1,i):
            print('No')
            exit()

print('Yes')