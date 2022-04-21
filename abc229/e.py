class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]
    

    def same(self, x, y):
        return self.root(x) == self.root(y)
    
    def union(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return 
        else:
            self.parents[rx] += self.parents[ry]
            self.parents[ry] = rx
    
N,M = map(int,input().split())

graph = [[] for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)

uf = UnionFind(N)
cur = 0
ans = [cur]
for i in range(N-1,0,-1):
    cur += 1
    for j in graph[i]:
        if not uf.same(i,j):
            uf.union(i,j)
            cur -= 1
    ans.append(cur)


for i in range(N-1,-1,-1):
    print(ans[i])