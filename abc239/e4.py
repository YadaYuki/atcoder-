from sys import setrecursionlimit
setrecursionlimit(10**6)
N,Q = map(int,input().split())
X = list(map(int,input().split()))
tree = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)


def dfs(p,c):
    is_leaf = len(tree[c]) == 1 and c != 0
    if is_leaf:
        children_numbers[c] = [X[c]]
    else:
        children_numbers[c].append(X[c])
        for i in tree[c]:
            if i != p:
                children_numbers[c].extend(dfs(c,i))
        children_numbers[c].sort(reverse=True)
        children_numbers[c] = children_numbers[c][:20]
    return children_numbers[c]

children_numbers = [[] for _ in range(N)]

dfs(-1,0)

for _ in range(Q):
    v,k = map(int,input().split())
    print(children_numbers[v-1][k-1])
