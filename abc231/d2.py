import sys
sys.setrecursionlimit(10**6)

N,M = map(int, input().split())
parents = [-1 for _ in range(N)]
neighbors = [0 for _ in range(N)]

def union(x,y):
    if is_same(x,y):
        return
    x_root = find(x)
    y_root = find(y)
    parents[y_root] = x_root
    
def is_same(x,y):
    x_root = find(x)
    y_root = find(y)
    return x_root == y_root


def find(x):
    if parents[x] == -1:
        return x
    parents[x] = find(parents[x])
    return parents[x]



for _ in range(M):
    a,b = map(int, input().split())
    neighbors[a-1] += 1
    neighbors[b-1] += 1
    if neighbors[a-1] > 2 or neighbors[b-1] > 2:
        print('No')
        exit()
    if is_same(a-1,b-1):
        print('No')
        exit()
    union(a-1,b-1)
        
print('Yes')    


