import sys
sys.setrecursionlimit(1000000)

N,M = map(int,input().split())

G = [[] for _ in range(N)]
visited = []

for i in range(M):
  A,B = map(int,input().split())
  G[A-1].append(B-1)

def dfs(i):
  visited[i] = True
  for node in G[i]:
    if visited[node] == False:

      dfs(node)    

ans = 0

for i in range(N):
  visited = [False] * N
  dfs(i)
  ans += sum(visited)
print(ans)
