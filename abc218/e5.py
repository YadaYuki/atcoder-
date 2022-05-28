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

uf = UnionFind(N)

edges = [list(map(int,input().split())) for i in range(M)]


edges.sort(key=lambda x:x[2])

ans = sum([edges[i][2] for i in range(M)])
for edge in edges:
    a,b,c = edge[0]-1,edge[1]-1,edge[2]
    if not uf.same(a,b):
        uf.unite(a,b)
        ans -= c
    elif c < 0:
        ans -= c

print(ans)
        

