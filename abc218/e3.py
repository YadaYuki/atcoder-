import sys
sys.setrecursionlimit(2*10**5 + 1)

class UnionFind:
    def __init__(self,N):
        self.__parents_or_size = [-1 for i in range(N)]
    
    def root(self,x):
        if self.__parents_or_size[x] < 0:
            return x
        else:
            self.__parents_or_size[x] = self.root(self.__parents_or_size[x])
            return self.__parents_or_size[x]
    
    def same(self,x,y):
        return self.root(x) == self.root(y)
    
    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        self.__parents_or_size[x] += self.__parents_or_size[y]
        self.__parents_or_size[y] = x


N,M = map(int,input().split())
edges = []
for i in range(M):
    a,b,c = map(int, input().split())
    edges.append([a-1,b-1,c])

uf = UnionFind(N)

edges.sort(key=lambda x:x[2])

gs_G_min = 0

for i in range(len(edges)):
    a,b,c = edges[i]
    if not uf.same(a,b):
        uf.unite(a,b)
        gs_G_min += c
    elif c < 0:
        gs_G_min += c

gs_G = sum([edges[i][2] for i in range(M)])

ans = gs_G - gs_G_min

print(ans)

