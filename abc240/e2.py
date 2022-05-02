# pypy3は再帰が遅いので、python3で実行する
import sys
sys.setrecursionlimit(10**6)
N = int(input())

tree = [[] for _ in range(N)]

id = 1
def dfs(p,c):
    if len(tree[c]) == 1 and c != 0:
        global id
        L[c] = id
        R[c] = id
        id += 1
    else:
        for n in tree[c]:
            if n != p:
                dfs(c,n)
                L[c] = min(L[c], L[n])
                R[c] = max(R[c], R[n])


for _ in range(N-1):
    u,v = map(int, input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)
BIG = 10**9
L = [BIG]*N
R = [-1]*N

dfs(-1,0)

for i in range(N):
    print(L[i],R[i])