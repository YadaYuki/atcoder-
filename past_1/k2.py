import sys
sys.setrecursionlimit(1000000)

N = int(input())

president = -1
tree = []
for  _ in range(N):
    tree.append([])

for i in range(N):
    p = int(input())
    if p == -1:
        president = i
        continue
    tree[p-1].append(i)

Q = int(input())
queries = []
for  _ in range(N):
    queries.append([])

for i in range(Q):
    a,b = map(int,input().split())
    queries[a-1].append([i,b-1]) # ボスかどうかを判定しなくてはならない対象.

ans = [False for _ in range(Q)]

boss = [False for _ in range(N)] # a[i]にとってjがbossかどうか


def dfs(a): # iのボスが誰か & iの部下に対する探索

    for q,b in queries[a]:
        ans[q] = boss[b]
    

    boss[a] = True

    for i in tree[a]:
        dfs(i)
    
    boss[a] = False


dfs(president)

for i in range(Q):
    if ans[i]:
        print("Yes")
    else:
        print("No")

