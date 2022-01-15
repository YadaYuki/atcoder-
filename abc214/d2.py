# memo:https://scrapbox.io/AtCoderPracticeMemo/ABC214_D_-_Sum_of_Maximum_Weights
import sys
sys.setrecursionlimit(10**6)

N = int(input())
parents = [-1] * N # 各ノードは全て独立しており、それぞれが属する部分木のsizeは1なので初期値は-1

def union(x,y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    parents[x] += parents[y] # xの親にyをつなぐ...
    parents[y] = x


def root(x):
    if parents[x] < 0:
        return x
    parents[x] = root(parents[x])
    return parents[x]

def size(x):
    x_root = root(x)
    return -parents[x_root]

edges = []
for _ in range(N-1):
    u,v,w = map(int, input().split())
    edges.append([w,u-1,v-1])

edges.sort()

ans = 0

for edge in edges:
    w,u,v = edge
    ans += w * size(u) * size(v)
    union(u,v)
    

print(ans)



