import sys
sys.setrecursionlimit(2*10**5 + 1)

class UnionFind:
    def __init__(self,N):
        self.__parents_or_size = [-1 for i in range(N)]
    
    def root(self,x):
        if self.__parents_or_size[x] < 0:
            return x
        else:
            self.__parents_or_size[x] = self.root(self.__parents_or_size[x])
            return self.__parents_or_size[x]
    
    def same(self,x,y):
        return self.root(x) == self.root(y)
    
    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        self.__parents_or_size[x] += self.__parents_or_size[y]
        self.__parents_or_size[y] = x


if __name__ == "__main__":
    N,M = map(int,input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    
    uf = UnionFind(N)

    connected_components = 0
    ans = [connected_components]
    for node in range(N-1,0,-1):
        connected_components += 1
        for node_next in G[node]:
            if (not uf.same(node,node_next)) and node < node_next:
                uf.unite(node,node_next)
                connected_components -= 1
        ans.append(connected_components)
    ans.reverse()
    for i in ans:
        print(i)
