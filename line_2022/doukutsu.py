



def dfs(depth,prev,curr):

    visited[curr] = True
    if depth >= 3 :
        return 
    else:
        for n in graph[curr]:
            if n != prev and not visited[n]:
                dfs(depth+1,curr,n)

def solve(N,P):
    global graph
    global visited
    graph = [[] for _ in range(N)]
    for i,p in enumerate(P):
        graph[i+1].append(p-1)
        graph[p-1].append(i+1)
    ans = []
    visited = [False]*N
    for i in range(N):
        visited = [False]*N
        dfs(0,-1,i)
        ans.append(sum(visited))
    
    print(*ans)




N = int(input())
P = list(map(int,input().split()))
graph = None
visited = None
solve(N, P)