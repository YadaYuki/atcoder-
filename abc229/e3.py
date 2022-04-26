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
G = [[] for i in range(N)]
for _ in range(M):
    A,B = map(int,input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

uf = UnionFind(N)

ans = [0]
cur = 0
for i in range(N-1,0,-1):
    cur += 1
    for j in G[i]:
        if (not uf.same(i,j)) and i < j:
            uf.unite(i,j)
            cur -= 1
    ans.append(cur)

ans.reverse()
for i in ans:
    print(i)