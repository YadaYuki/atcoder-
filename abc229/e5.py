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
    uf = UnionFind(N+1)
    graph = [[] for i in range(N)]
    for i in range(M):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
    
    cur_connected_component = 0
    ans = [cur_connected_component]
    for node in  range(N-1,0,-1):
        cur_connected_component += 1
        for next_node in graph[node]:
            if uf.same(node,next_node):
                continue
            else:
                uf.unite(node,next_node)
                cur_connected_component -= 1
        ans.append(cur_connected_component)
    
    ans.reverse()
    for i in ans:
        print(i)
            
