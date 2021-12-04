import sys
sys.setrecursionlimit(1000000)

N = int(input())

graph = [[] for _ in range(N)]

for _ in range(N-1):
    A,B = map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)


ans = []
visited = [False for _ in range(N)]
visited_town_num = [0 for _ in range(N)]

def dfs(town):
    ans.append(town)
    visited[town] = True
    for i in range(visited_town_num[town],len(graph[town])):
        town_next_to = graph[town][i]
        if not visited[town_next_to] :
            visited_town_num[town] = i
            dfs(town_next_to)
    
    if town == 0:
        return 
    else:
        dfs(ans[-2])

dfs(0)

for i in range(len(ans)):
    print(ans[i]+1,end=' ')




