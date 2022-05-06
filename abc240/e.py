import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
  u,v = map(int,input().split())
  tree[u-1].append(v-1)
  tree[v-1].append(u-1)


def dfs(p,n):
  global id
  if len(tree[n]) == 1 and n != 0:
    LR[n] = [id,id]
    id += 1
  else:
    for i in tree[n]:
      if i != p:
        dfs(n,i)
        L[v] = min(L[v], L[nv])
        R[v] = max(R[v], R[nv])

    r = tree[n][(len(tree[n])-1)]
    l = tree[n][0]
    
    if r == p:
      r = tree[n][(len(tree[n])-2)]
    if l == p:
      l = tree[n][1]
    LR[n] = [LR[l][0],LR[r][1]]
    

LR = [None] * N
id = 1

dfs(-1,0)




for i in range(N):
  print(LR[i][0],LR[i][1])

