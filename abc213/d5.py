import sys
sys.setrecursionlimit(10**6)
N = int(input())
graph = [[] for _ in range(N)]
for i in range(N-1):
    A,B = map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

for i in range(N):
    graph[i].sort()

visited = [False] * N
ans = []
def dfs(town:int):
    visited[town] = True
    ans.append(town+1)
    for next_to in graph[town]:
        if visited[next_to]:
            continue
        dfs(next_to)
        ans.append(town+1)
dfs(0)

print(*ans)

