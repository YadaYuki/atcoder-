import sys
sys.setrecursionlimit(10**6)
class UnionFind():
    def __init__(self,n:int):
        self.__parent_or_size = [-1 for i in range(n)]
    
    def find(self,x):
        if self.__parent_or_size[x] < 0:
            return x
        else:
            self.__parent_or_size[x] = self.find(self.__parent_or_size[x])
            return self.__parent_or_size[x]
    
    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root==y_root:
            return
        self.__parent_or_size[x_root] += self.__parent_or_size[y_root]
        self.__parent_or_size[y_root] = x_root
    
    def is_same(self,x,y):
        return self.find(x)==self.find(y)



N,M = map(int,input().split())
uf = UnionFind(N)
graph = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    if uf.is_same(a-1,b-1):
        print('No')
        exit()
    uf.union(a-1, b-1)
for i in range(N):
    if len(graph[i]) > 2:
        print('No')
        exit()

print('Yes')