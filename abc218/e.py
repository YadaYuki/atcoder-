import sys
sys.setrecursionlimit(10 ** 6)
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]
    

    def same(self, x, y):
        return self.root(x) == self.root(y)
    
    def union(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return 
        else:
            self.parents[rx] += self.parents[ry]
            self.parents[ry] = rx


if __name__ == "__main__":
    N,M = map(int, input().split())
    uf = UnionFind(N)
    edges = []
    ans = 0
    for _ in range(M):
        A,B,C = map(int, input().split())
        ans += C
        edges.append((A-1,B-1,C))
    
    edges.sort(key=lambda x:x[2])
    for edge in edges:
        a,b,c = edge
        if not uf.same(a,b):
            uf.union(a,b)
            ans -= c
        elif c < 0:
            ans -= c
    print(ans)
