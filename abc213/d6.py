import sys
sys.setrecursionlimit(2*10**5 + 1)


N = int(input())
graph = [[] for _ in range(N)]

for _ in range(N-1):
    A,B = map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

for i in range(N):
    graph[i].sort()



ans = []
visited = [False]*N
def dfs(prev,cur):
    visited[cur] = True
    ans.append(cur+1)
    for next_node in graph[cur]:
        if next_node == prev:
            continue
        if visited[next_node]:
            continue
        dfs(cur,next_node)
        ans.append(cur+1)


dfs(-1,0)

print(*ans)
