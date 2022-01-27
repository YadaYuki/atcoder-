

N = int(input())
tree = []

for i in range(N-1):
    u,v,w = map(int, input().split())
    tree.append([w,u-1,v-1])

class UnionFind:
    def __init__(self,size):
        self.__size_or_parent = [-1 for _ in range(size)]
    
    def find(self,x):
        if self.__size_or_parent[x] < 0:
            return x
        self.__size_or_parent[x] = self.find(self.__size_or_parent[x])
        return self.__size_or_parent[x]
    
    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.__size_or_parent[x_root] += self.__size_or_parent[y_root]  
            self.__size_or_parent[y_root] = x_root
    
    def size(self,x):
        return -1 * self.__size_or_parent[self.find(x)]


tree.sort()
uf = UnionFind(N)

ans = 0
for i in range(N-1):
    w,u,v = tree[i]
    ans += w * uf.size(u) * uf.size(v)
    uf.union(u,v)

print(ans)