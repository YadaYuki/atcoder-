


MAX_K  = 20
def dfs(p,c):
    nodes_in_subtree_X[c].append(X[c])

    for n in tree[c]:
        if n != p:
            dfs(c,n)
            nodes_in_subtree_X[c].extend(nodes_in_subtree_X[n])
    
    nodes_in_subtree_X[c].sort(reverse=True)
    nodes_in_subtree_X[c] = nodes_in_subtree_X[c][:MAX_K]


N,Q = map(int,input().split())
X = list(map(int,input().split()))
tree = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

nodes_in_subtree_X = [[] for _ in range(N)] # 子ノードのXの値(先頭MAX_K個)

dfs(-1,0)

for i in range(Q):
    v,k = map(int,input().split())
    v -= 1
    k -= 1
    print(nodes_in_subtree_X[v][k])