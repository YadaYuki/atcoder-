from sys import setrecursionlimit
setrecursionlimit(10**9)

N,X,Y = map(int,input().split())
tree = [list() for i in range(N)]

for i in range(N-1):
    u,v = map(int,input().split())
    u-=1
    v-=1
    tree[u].append(v)
    tree[v].append(u)


ans = list()
visited = [False] * N
def dfs(prev,cur) -> bool:
    visited[cur] = True
    if cur == Y - 1:
        ans.append(cur + 1)
        return True
    
    for n in tree[cur]:
        if n == prev:
            continue
        if visited[n]:
            continue
        if dfs(cur,n):
            ans.append(cur + 1)
            return True

    return False

dfs(-1,X-1)
ans.reverse()
print(*ans)