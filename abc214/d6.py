class UnionFind:
    def __init__(self, n):
        self.__parents_or_size = [-1 for i in range(n)]

    def root(self, x):
        if self.__parents_or_size[x] < 0:
            return x
        self.__parents_or_size[x] = self.root(self.__parents_or_size[x])
        return self.__parents_or_size[x]
    
    def union(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx != ry:
            self.__parents_or_size[rx] += self.__parents_or_size[ry]
            self.__parents_or_size[ry] = rx
    

    def size(self, x):
        return -self.__parents_or_size[self.root(x)]

N = int(input())

tree = []

for _ in range(N-1):
    u,v,w = map(int, input().split())
    tree.append([w,u-1,v-1])

tree.sort()

uf = UnionFind(N)

ans = 0

for i in range(N-1):
    w,u,v = tree[i]
    ans += w * uf.size(u) * uf.size(v)
    uf.union(u,v)

print(ans)