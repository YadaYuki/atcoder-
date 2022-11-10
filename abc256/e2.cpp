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
    int N;
    cin >> N;
    vector<ll> X(N);
    vector<ll> C(N);
    for (int i = 0; i < N; i++)
    {
        cin >> X[i];
    }
    for (int i = 0; i < N; i++)
    {
        cin >> C[i];
    }
    auto uf = UnionFind(N + 1);
    ll ans = 0;
    for (int i = 0; i < N; i++)
    {
        auto x = X[i];
        if (!uf.is_same(i, x - 1))
        {
            uf.unite(i, x - 1);
            continue;
        }
        // 閉路が存在する
        auto v = i;
        ll c = 1e10;
        do
        {
            c = min(c, C[v]);
            v = X[v] - 1;
        } while (v != i);
        ans += c;
    }
    cout << ans << endl;
}