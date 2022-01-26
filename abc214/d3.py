
class UnionFind:
    def __init__(self,size):
        self.size_or_parent = [-1 for _ in range(size)]
    
    def find(self,x):
        if self.size_or_parent[x] < 0:
            return x
        self.size_or_parent[x] = self.find(self.size_or_parent[x])
        return self.size_or_parent[x]
    
    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            pass
        self.size_or_parent[x_root] += self.size_or_parent[y_root]
        self.size_or_parent[y_root] = x_root

    def size(self,x):
        return -self.size_or_parent[self.find(x)]
    

if __name__ == '__main__':
    N = int(input())
    tree = [] # [w,u,v]

    for _ in range(N-1):
        u,v,w = map(int, input().split())
        tree.append([w,u-1,v-1])
    tree.sort()
    union_find = UnionFind(N)
    ans = 0
    for edge in tree:
        w,u,v = edge
        ans += union_find.size(u) * union_find.size(v) * w
        union_find.union(u,v)
    print(ans)


