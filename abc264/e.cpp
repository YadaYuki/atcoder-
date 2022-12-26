#include <bits/stdc++.h>
#define ll long long
using namespace std;

class UnionFind
{
private:
    vector<long long> parent_or_size;
    long long N;

public:
    UnionFind(long long s)
    {
        N = s;
        parent_or_size.assign(N, -1);
    }
    long long root(long long x)
    {
        if (parent_or_size[x] < 0)
        {
            return x;
        }
        parent_or_size[x] = root(parent_or_size[x]);
        return parent_or_size[x];
    }
    long long is_same(long long x, long long y)
    {
        return root(x) == root(y);
    }
    long long size(long long x)
    {
        return -parent_or_size[root(x)];
    }
    void unite(long long x, long long y)
    {
        long long rx = root(x);
        long long ry = root(y);
        if (rx == ry)
        {
            return;
        }
        parent_or_size[rx] += parent_or_size[ry];
        parent_or_size[ry] = rx;
    }
};

int main()
{
    int N, M, E;
    cin >> N >> M >> E;
    vector<pair<int, int>> uv;
    for (int i = 0; i < E; i++)
    {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        uv.push_back({u, v});
    }
    int Q;
    cin >> Q;
    vector<int> X(Q);
    set<int> X_set;
    for (int i = 0; i < Q; i++)
    {
        int x;
        cin >> x;
        x--;
        X[i] = x;
        X_set.insert(x);
    }
    vector<bool> ELECTIRCS(N + M);
    for (int i = N; i < N + M; i++)
    {
        ELECTIRCS[i] = true;
    }
    auto uf = UnionFind(N + M);
    int electrics_cnt = 0;
    for (int i = 0; i < E; i++)
    {
        if (X_set.find(i) != X_set.end())
        {
            continue;
        }
        auto uvi = uv[i];
        auto u = uvi.first;
        auto v = uvi.second;
        if (uf.is_same(u, v))
        {
            continue;
        }
        auto ru = uf.root(u);
        auto rv = uf.root(v);

        if (ELECTIRCS[ru] && !ELECTIRCS[rv])
        {
            // rvが新たに感電
            ELECTIRCS[rv] = true;
            electrics_cnt += uf.size(rv);
        }
        if (!ELECTIRCS[ru] && ELECTIRCS[rv])
        {
            // ruが新たに感電
            ELECTIRCS[ru] = true;
            electrics_cnt += uf.size(ru);
        }
        uf.unite(u, v);
    }
    vector<int> ans;
    ans.push_back(electrics_cnt);
    for (int i = X.size() - 1; i > 0; i--)
    {
        auto x = X[i];
        auto uvx = uv[x];
        auto u = uvx.first;
        auto v = uvx.second;
        if (uf.is_same(u, v))
        {
            ans.push_back(electrics_cnt);
            continue;
        }
        auto ru = uf.root(u);
        auto rv = uf.root(v);

        if (ELECTIRCS[ru] && !ELECTIRCS[rv])
        {
            // rvが新たに感電
            ELECTIRCS[rv] = true;
            electrics_cnt += uf.size(rv);
        }
        if (!ELECTIRCS[ru] && ELECTIRCS[rv])
        {
            // ruが新たに感電
            ELECTIRCS[ru] = true;
            electrics_cnt += uf.size(ru);
        }
        ans.push_back(electrics_cnt);
        uf.unite(u, v);
    }
    for (int i = ans.size() - 1; i >= 0; i--)
    {
        cout << ans[i] << endl;
    }
}