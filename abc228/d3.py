

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.parents[ry] = rx



if __name__ == "__main__":
    Q = int(input())
    N = (2**20)
    uf = UnionFind(N) # -1ではない区間の集合を管理する。最も右端が親→ 2のステップの計算量を抑えるため.
    A = [-1] * N
    for _ in range(Q):
        t,x = map(int, input().split())
        if t == 1:
            h = x % N
            while A[h] != -1:
                h = uf.find(h) + 1
                if h == N:
                    h = 0
                    continue
                uf.union(h, h-1)
            A[h] = x
        else:
            print(A[x%N])


    

        