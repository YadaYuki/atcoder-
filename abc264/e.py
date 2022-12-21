import sys
sys.setrecursionlimit(10**6)
class UnionFind:
    def __init__(self,size:int):
        self.__size = size
        self.__parent_or_size = [
            -1 for i in range(size + 1)
        ]
    
    def union(self,u,v):
        if self.same(u, v):
            return 
        ru = self.root(u)
        rv = self.root(v)
        self.__parent_or_size[ru] += self.__parent_or_size[rv]
        self.__parent_or_size[rv] = ru
    
    def size(self,u):
        return -self.__parent_or_size[self.root(u)]

    def root(self,u):
        if self.__parent_or_size[u] < 0:
            return u
        
        self.__parent_or_size[u] = self.root(self.__parent_or_size[u])

        return self.__parent_or_size[u]
    
    def same(self,u,v):
        return self.root(u) == self.root(v)

N,M,E = map(int,input().split())
uv = []
for i in range(E):
    u,v = map(int,input().split())
    u-=1
    v-=1
    uv.append([u,v])

Q = int(input())
x = [int(input())-1 for i in range(Q)]
xset = set(x)
uf = UnionFind(N+M+1)

electricity_passes = [False for i in range(N+M)]
for i in range(N,N+M):
    electricity_passes[i] = True
cur = 0
for i in range(E):
    if i in xset:
        continue
    u,v = uv[i]
    if uf.same(u, v):
        continue
    ru,rv = uf.root(u),uf.root(v)
    if electricity_passes[ru] and electricity_passes[rv]:
        pass
    elif electricity_passes[ru]:
        cur += uf.size(rv) # こちら側(rv)の連結成分には町しかないから、街の数と考えていい。
        electricity_passes[rv] = True
    elif electricity_passes[rv]:
        cur += uf.size(ru) # こちら側(ru)の連結成分には町しかないから、街の数と考えていい。
        electricity_passes[ru] = True
    uf.union(u, v)

ans_reversed = [cur]
for i in range(Q-1,0,-1):
    u,v = uv[x[i]]
    if uf.same(u, v):
        pass
    ru = uf.root(u)
    rv = uf.root(v)
    if electricity_passes[ru] and electricity_passes[rv]:
        pass
    elif electricity_passes[ru]:
        cur += uf.size(rv) # こちら側(rv)の連結成分には町しかないから、街の数と考えていい。
        electricity_passes[rv] = True
    elif electricity_passes[rv]:
        cur += uf.size(ru) # こちら側(ru)の連結成分には町しかないから、街の数と考えていい。
        electricity_passes[ru] = True
    ans_reversed.append(cur)
    uf.union(u, v)

ans = reversed(ans_reversed)

for a in ans:
    print(a)



