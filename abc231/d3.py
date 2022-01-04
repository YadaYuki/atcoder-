import sys
sys.setrecursionlimit(10**6)



N,M = map(int,input().split())
parents = [-1] * N


def find(x):
    if parents[x] == -1:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px == py:
        return
    parents[py] = px

neighbors = [[] for _ in range(N)]

possible = True
for i in range(M):
    A,B = map(int,input().split())
    neighbors[A-1].append(B-1)
    neighbors[B-1].append(A-1)
    if find(A-1) == find(B-1):
        possible = False
    else:
        union(A-1,B-1)

for i in range(N):
    if len(neighbors[i]) > 2:
        possible = False

if possible:
    print("Yes")
else:
    print("No")








