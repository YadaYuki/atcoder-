import sys
sys.setrecursionlimit(10**6)
N = int(input())
tree = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
L = [-1] * N
R = [-1] * N
idx = 1
def dfs(p,c):
    is_leaf = len(tree[c]) == 1 and c!=0
    if is_leaf:
        global idx
        L[c] = idx
        R[c] = idx
        idx += 1
    else:
        for i in tree[c]:
            if i != p:
                dfs(c,i)
        L[c] = L[tree[c][0] if tree[c][0] != p else tree[c][1]]
        R[c] = R[tree[c][-1] if tree[c][-1] != p else tree[c][-2]]

dfs(-1,0)



for i in range(N):
    print(L[i], R[i])
