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

N = int(input())
X = list(map(int,input().split()))
C = list(map(int,input().split()))
X = [x-1 for x in X]
directed_graph = [[] for i in range(N)]

for i,x in enumerate(X):
    directed_graph[i].append(x-1)

uf = UnionFind(N+1)
ans = 0
for i in range(N):
    if not uf.same(i, X[i]):
        uf.unite(i, X[i])
    else:
        n = i
        min_stress = 1e10
        while True:
            min_stress = min(min_stress,C[n])
            n = X[n]
            if n == i:
                break
        ans += min_stress

print(ans)