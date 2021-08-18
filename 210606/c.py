import sys
from typing import Tuple
sys.setrecursionlimit(100000)

N,M = map(int,input().split())
G = [[] for _ in range(N)]

for i in range(M):
  A,B = map(int,input().split())
  G[A-1].append(B-1)

visited = []

def dfs(i):
  visited[i] = True
  for node in G[i]:
    if visited[node] == False:
      visited[node] = True
      dfs(node)
      
ans = 0
for i in range(N):
  visited = [False] * N
  dfs(i)
  ans += sum(visited)

print(ans)

