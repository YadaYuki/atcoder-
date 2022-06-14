import sys

"""ややTLが怪しいので、高速な入力のreadlineを使うと良いです（改行文字も受け取るので注意）"""
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # 再帰上限を上げないとREになります


def main():
    MAX_K = 20

    def dfs(u, p):
        L[u].append(X[u])  # 自分自身に書かれた整数です
        for v in G[u]:
            if v == p:
                continue
            dfs(v, u)
            L[u].extend(L[v])  # uの子vの部分木の整数をすべてuに追加します
        L[u].sort(reverse=True)  # 大きい順なので、reverse=Trueです
        L[u] = L[u][:MAX_K]  # 20個に減らします

    N, Q = map(int, readline().split())
    X = [0] + list(map(int, readline().split()))
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, readline().split())
        G[a].append(b)
        G[b].append(a)
    L = [[] for _ in range(N + 1)]  # 頂点iの部分木に書かれた整数を大きい順に最大20個記憶
    dfs(1, 0)

    for _ in range(Q):
        v, k = map(int, readline().split())
        print(L[v][k - 1])


main()

