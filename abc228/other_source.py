# https://atcoder.jp/contests/abc228/submissions/28276698

from sys import setrecursionlimit, stdin
 
setrecursionlimit(1000000)
 
 
class UnionFind:
    def __init__(self, n):
        self._n = n
        self._root_or_size = [-1 for _ in range(n)]
 
    def find(self, i):
        if self._root_or_size[i] < 0:
            return i
        self._root_or_size[i] = self.find(self._root_or_size[i])
        return self._root_or_size[i]
 
    def unite(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri == rj:
            return ri
        if ri < rj:
            ri, rj = rj, ri
        self._root_or_size[ri] += self._root_or_size[rj]
        self._root_or_size[rj] = ri # iをjの親とする
        return ri
 
    def same(self, i, j):
        return self.find(i) == self.find(j)
 
    def size(self, i):
        return -self._root_or_size[self.find(i)]
 
    def groups(self):
        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[self.find(i)].append(i)
        return [x for x in result if x]
 
 
def main():
    q = int(stdin.readline().rstrip())
    tx = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(q)]
    n = 1 << 20
    ans = [-1 for _ in range(n)] # N= 2 ** 20からなる数列を初期化.
    uf = UnionFind(n)
    for t, x in tx:
        if t == 1:
            h = x % n
            if ans[h] == -1:
                ans[h] = x
                continue
            while True:
                h = uf.find(h) + 1 # Q. + 1はなんだろう？
                
                if h == n: # 数列の最後に来たら、一番初めに戻る.
                    h = 0
                    if ans[h] == -1:
                        break
                    else:
                        continue
                
                uf.unite(h - 1, h) # 要素間の仕切りを管理している. 仕切りの右端をrootの親とするようなUnionFind木を作る.

                if ans[h] == -1:
                    break

            ans[h] = x
        else:
            print(ans[x % n])
 
 
if __name__ == '__main__':
    main()