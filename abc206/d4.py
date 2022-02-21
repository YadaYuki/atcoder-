class UnionFind:
    def __init__(self, n):
        self.parent_or_size = [-1 for i in range(n)]

    def find(self, x):
        if self.parent_or_size[x] < 0:
            return x
        else:
            self.parent_or_size[x] = self.find(self.parent_or_size[x])
            return self.parent_or_size[x]
    
    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.parent_or_size[rx] += self.parent_or_size[ry]
            self.parent_or_size[ry] = rx



if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    uf = UnionFind(2*10**5+1)
    for i in range(N//2):
        if A[i] != A[N-1-i]:
            uf.union(A[i], A[N-1-i])
    

    ans = 0
    for i in range(2*10**5+1):
        if uf.parent_or_size[i] < 0:
            ans += uf.parent_or_size[i] + 1
    
    print(-ans)

