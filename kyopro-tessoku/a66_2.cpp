#include <bits/stdc++.h>
using namespace std;

class UnionFind
{
private:
    vector<int> parent_or_size;
    int size;

public:
    explicit UnionFind(int s)
    {
        parent_or_size.assign(s, -1);
        size = s;
    }

    int root(int u)
    {
        if (parent_or_size[u] < 0)
        {
            return u;
        }
        parent_or_size[u] = root(parent_or_size[u]);
        return parent_or_size[u];
    }

    bool same(int u, int v)
    {
        auto ru = root(u);
        auto rv = root(v);
        return ru == rv;
    }

    void unite(int u, int v)
    {
        auto ru = root(u);
        auto rv = root(v);
        if (ru != rv)
        {
            parent_or_size[ru] += parent_or_size[rv];
            parent_or_size[rv] = ru;
        }
    }
};

int main()
{
    int N, Q;
    cin >> N >> Q;
    auto uf = UnionFind(N);
    for (int i = 0; i < Q; i++)
    {
        int q, u, v;
        cin >> q >> u >> v;
        u--;
        v--;
        if (q == 1)
        {
            uf.unite(u, v);
        }
        if (q == 2)
        {
            cout << (uf.same(u, v) ? "Yes" : "No") << endl;
        }
    }
}