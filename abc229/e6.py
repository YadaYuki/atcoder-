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
    directed_graph = [[] for i in range(N)] # idxの小さい方から大きい方へと辺が伸びている有向グラフ
    for _ in range(M):
        a,b = map(int,input().split())
        directed_graph[a-1].append(b-1)

    uf = UnionFind(N+1)
    cur_connected_component = 0 # 現在の有向グラフにおける接続成分数。全ての頂点が消えているので、初期値は0
    ans = [cur_connected_component]
    for i in range(N-1,0,-1):
        cur_connected_component += 1
        for j in range(len(directed_graph[i])):
            if not uf.same(i,directed_graph[i][j]):
                uf.unite(i,directed_graph[i][j])
                cur_connected_component -= 1
        ans.append(cur_connected_component)

    ans.reverse()

    for i in ans:
        print(i)