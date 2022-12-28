#include <bits/stdc++.h>
#define ll long long
using namespace std;

class UnionFind
{
private:
    vector<long long> parent_or_size;
    long long size;

public:
    UnionFind(long long s)
    {
        size = s;
        parent_or_size.assign(size, -1);
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
    ll N;
    cin >> N;
    vector<ll> X(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> X[i];
        X[i]--;
    }
    vector<ll> C(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> C[i];
    }
    auto uf = UnionFind(N + 1);
    ll ans = 0;
    for (ll n = 0; n < N; n++)
    {
        auto next = X[n];
        if (!uf.is_same(n, next))
        {
            uf.unite(n, next);
        }
        else
        {
            ll min_frustration = 10000000000;
            auto start = next;
            auto cur = next;
            do
            {
                min_frustration = min(C[cur], min_frustration);
                cur = X[cur];
            } while (cur != start);
            ans += min_frustration;
        }
    }
    cout << ans << endl;
}