



N = int(input())
graph = [[] for _ in range(N)]

for i in range(N-1):
    A,B = map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

visited = [False] * N

ans = []
def dfs(town:int):
    # ここ？
    visited[town] = True
    ans.append(town+1)
    for town_next_to in graph[town]:
        if not visited[town_next_to]:
            
            dfs(town_next_to)
            ans.append(town+1)

dfs(0)


print(*ans)

