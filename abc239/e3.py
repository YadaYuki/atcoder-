N,Q = map(int,input().split())
X = list(map(int,input().split()))

graph = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

MAX_K = 20

def dfs(p,c):
    subtrees_X[c].append(X[c])
    for n in graph[c]:
        if n != p:
            dfs(c,n)
            subtrees_X[c].extend(subtrees_X[n])
    subtrees_X[c].sort(reverse=True) # 降順にソート
    subtrees_X[c] = subtrees_X[c][:MAX_K] # MAX_K個の要素を残す



subtrees_X = [[] for _ in range(N)] # ノードiのサブツリーの各ノードのXの値

dfs(-1, 0)

for _ in range(Q):
    v,k = map(int,input().split())
    v -= 1
    k -= 1
    print(subtrees_X[v][k])