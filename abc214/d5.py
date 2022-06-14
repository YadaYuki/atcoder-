class UnionFind:
    def __init__(self,size):
        self.__parents_or_size = [-1 for i in range(size)]
    

    def find(self,x):
        if self.__parents_or_size[x] < 0:
            return x
        else:
            self.__parents_or_size[x] = self.find(self.__parents_or_size[x])
            return self.__parents_or_size[x]
    
    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.__parents_or_size[rx] += self.__parents_or_size[ry]
            self.__parents_or_size[ry] = rx
    


    def size(self,x):
        return -self.__parents_or_size[self.find(x)]
    

N = int(input())
uf = UnionFind(N)
tree = []
for i in range(N-1):
    u,v,w = map(int,input().split())
    tree.append([w,u-1,v-1])

tree.sort()

ans = 0

for i in range(N-1):
    w,u,v = tree[i]
    ans += w * uf.size(u) * uf.size(v)
    uf.union(u,v)


print(ans)