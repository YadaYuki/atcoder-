import sys
sys.setrecursionlimit(10**6)
N = int(input())
tree = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

cur_idx = 1
def dfs(p,c):
    global cur_idx
    if c != 0 and len(tree[c]) == 1:
        L[c] = cur_idx
        R[c] = cur_idx
        cur_idx += 1
    else:
        for i in tree[c]:
            if i != p:
                dfs(c, i)
        L[c] = L[tree[c][0]]
        if p == tree[c][0]:
            L[c] = L[tree[c][1]]
        R[c] = R[tree[c][-1]]
        if p == tree[c][-1]:
            R[c] = R[tree[c][-2]]



L = [-1]*N
R = [-1]*N


dfs(-1,0)

for i in range(N):
    print(L[i],R[i])
