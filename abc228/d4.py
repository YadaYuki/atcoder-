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


if __name__ == "__main__":
    Q = int(input())
    N = 2 ** 20
    uf = UnionFind(N)
    A = [-1 for _ in range(N)]
    for _ in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            h = x % N
            while A[h] != -1:
                h = uf.find(h) + 1
                if h == N:
                    h = 0
                    continue
            uf.union(h,h-1)
            A[h] = x

        else:
            print(A[x%N])
            pass