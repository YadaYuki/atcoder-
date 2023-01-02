from sys import setrecursionlimit
setrecursionlimit(2*(10**6))
N,X,Y = map(int,input().split())
tree = [[] for i in range(N)]
X-=1
Y-=1
for i in range(N-1):
    u,v = map(int,input().split())
    u-=1
    v-=1
    tree[u].append(v)
    tree[v].append(u)
ans = list()
def dfs(prev,cur) -> bool:
    visited[cur] = True
    if cur == Y:
        ans.append(Y + 1)
        return True
    else:
        for n in tree[cur]:
            if n != prev:
                if dfs(cur,n):
                    ans.append(cur + 1)
                    return True
                    
visited = [False for i in range(N)]
dfs(-1,X)
ans.reverse()
print(*ans)
