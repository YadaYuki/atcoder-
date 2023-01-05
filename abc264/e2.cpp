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
    ll N, M, E;
    cin >> N >> M >> E;
    vector<pair<ll, ll>> uv(E);
    for (ll i = 0; i < E; i++)
    {
        ll u, v;
        cin >> u >> v;
        u--;
        v--;
        uv[i] = {u, v};
    }
    ll Q;
    cin >> Q;
    vector<ll> X(Q);
    set<ll> X_set;
    for (ll i = 0; i < Q; i++)
    {
        cin >> X[i];
        X[i]--;
        X_set.insert(X[i]);
    }

    auto uf = UnionFind(N + M + 1);
    vector<bool> electrocuted(N + M);
    for (ll i = N; i < N + M; i++)
    {
        electrocuted[i] = true;
    }
    ll electrocuted_cities = 0;
    for (ll i = 0; i < E; i++)
    {
        if (X_set.find(i) != X_set.end())
        {
            continue;
        }
        auto u = uv[i].first;
        auto v = uv[i].second;
        if (uf.is_same(u, v))
        {
            continue;
        }
        auto ru = uf.root(u);
        auto rv = uf.root(v);
        if (electrocuted[ru] && !electrocuted[rv])
        {
            electrocuted_cities += uf.size(v);
            electrocuted[rv] = true;
        }
        if (!electrocuted[ru] && electrocuted[rv])
        {
            electrocuted_cities += uf.size(u);
            electrocuted[ru] = true;
        }
        uf.unite(u, v);
    }
    vector<ll> ans = {electrocuted_cities};
    for (ll i = Q - 1; i >= 0; i--)
    {
        auto x = X[i];
        auto u = uv[x].first;
        auto v = uv[x].second;
        if (uf.is_same(u, v))
        {
            ans.push_back(electrocuted_cities);
            continue;
        }
        auto ru = uf.root(u);
        auto rv = uf.root(v);
        if (electrocuted[ru] && !electrocuted[rv])
        {
            electrocuted_cities += uf.size(v);
            electrocuted[rv] = true;
        }
        if (!electrocuted[ru] && electrocuted[rv])
        {
            electrocuted_cities += uf.size(u);
            electrocuted[ru] = true;
        }
        ans.push_back(electrocuted_cities);
        uf.unite(u, v);
    }
    for (ll i = Q-1; i > -1; i--)
    {
        cout << ans[i] << endl;
    }
}