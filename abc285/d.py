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
ST = list()
ST_mp = {}
idx = 0
for i in range(N):
    s,t = input().split()
    ST.append([s,t])
    if s not in ST_mp:
        ST_mp[s] = idx
        idx += 1
    if t not in ST_mp:
        ST_mp[t] = idx
        idx += 1
graph = [[] for i in range(idx)]
for i in range(N):
    s,t = ST[i]
    graph[ST_mp[s]].append(ST_mp[t])

uf = UnionFind(2*10**5+1)

for i in range(N):
    s,t = ST[i]
    # graph[ST_mp[s]].append(ST_mp[t])
    si,ti = ST_mp[s],ST_mp[t]
    if uf.same(si, ti):
        print("No")
        exit()
    else:
        uf.unite(si, ti)

print("Yes")




