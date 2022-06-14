class UnionFind():
    def __init__(self,n):
        self.__parent_or_size=[-1 for _ in range(n)]
    
    def find(self,x):
        if self.__parent_or_size[x] < 0:
            return x
        self.__parent_or_size[x] = self.find(self.__parent_or_size[x])
        return self.__parent_or_size[x]
    
    def union(self,p,c):
        pr = self.find(p)   
        cr = self.find(c)
        if pr == cr:
            return
        self.__parent_or_size[pr] += self.__parent_or_size[cr] 
        self.__parent_or_size[cr] = pr



Q = int(input())
N = 2**20
A = [-1 for i in range(N)]
uf = UnionFind(N)

for i in range(Q):
    t,x = map(int,input().split())
    if t == 1:        
        idx = x % N
        if A[idx] != -1:
            idx = uf.find(idx) + 1
            if idx == N:
                idx = uf.find(0)
        uf.union(idx,idx-1)
        A[idx] = x
    elif t == 2:
        print(A[x%N])
        
