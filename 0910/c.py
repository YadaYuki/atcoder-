import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
# start_and_goal = [[False for _ in range(N)] for _ in range(N)]



for i in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)

temp = [False] * N

def dfs(node: int):
    temp[node] = True
    for node_next_to in graph[node]:
      if temp[node_next_to] == False:
        temp[node_next_to] = True
        dfs(node_next_to)
      

ans = 0
for i in range(N):
  temp = [False] * N
  dfs(i)
  ans += sum(temp)

print(ans)
