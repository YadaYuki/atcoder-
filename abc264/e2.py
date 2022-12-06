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
    
    def size(self,x):
        return -self.__parents_or_size[self.root(x)]
    
    def same(self,x,y):
        return self.root(x) == self.root(y)
    
    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        self.__parents_or_size[x] += self.__parents_or_size[y]
        self.__parents_or_size[y] = x



N,M,E = map(int,input().split())
uv = []
for i in range(E):
    u,v = map(int,input().split())
    u-=1
    v-=1
    uv.append([u,v])

Q = int(input())
X = [int(input())-1 for i in range(Q)]
X_set = set(X)
electrics = [False for i in range(N)] + [True for i in range(M)]
uf = UnionFind(N+M+1)

cur = 0
for i in range(E):
    
    if i in X_set:
        continue
    u,v = uv[i]
    
    ru,rv = uf.root(u),uf.root(v)
    
    if electrics[ru] and (not electrics[rv]):
        cur += uf.size(v)
        electrics[rv] = True
    
    elif electrics[rv] and (not electrics[ru]):
        cur += uf.size(u)
        electrics[ru] = True

    uf.unite(u, v)
ans = [cur]
for i in range(Q-1,0,-1):
    u,v = uv[X[i]]
    ru,rv = uf.root(u),uf.root(v)
    
    if electrics[ru] and (not electrics[rv]):
        cur += uf.size(v)
        electrics[rv] = True
    
    elif electrics[rv] and (not electrics[ru]):
        cur += uf.size(u)
        electrics[ru] = True
    ans.append(cur)
    uf.unite(u, v)

ans = reversed(ans)
for a in ans:
    print(a)




