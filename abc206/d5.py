N = int(input())
A = list(map(int, input().split()))

class UnionFind:
    def __init__(self,n):
        self.__parent_or_size = [-1 for i in range(n)]
    
    def find(self,x):
        if self.__parent_or_size[x] < 0:
            return x
        else:
            self.__parent_or_size[x] = self.find(self.__parent_or_size[x])
            return self.__parent_or_size[x]
    
    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.__parent_or_size[rx] += self.__parent_or_size[ry]
            self.__parent_or_size[ry] = rx
    
    def is_root(self,x):
        return self.__parent_or_size[x] < 0
    
    def size(self,x):
        return -self.__parent_or_size[self.find(x)]



uf = UnionFind(2*10**5+1)


for i in range(N//2):
    if A[i] != A[N-1-i]:
        uf.union(A[i], A[N-1-i])


ans = 0
for i in range(2*10**5+1):
    if uf.is_root(i):
        ans += uf.size(i) - 1

print(ans)