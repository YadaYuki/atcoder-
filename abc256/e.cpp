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
    vector<ll> X(N), C(N);
    for (auto &x : X)
    {
        cin >> x, --x;
    }
    for (auto &c : C)
    {
        cin >> c;
    }

    auto uf = UnionFind(N);
    ll ans = 0;
    for (int i = 0; i < N; i++)
    {
        // 嫌っている相手と同じ閉路に所属しているかどうか？
        if (!uf.is_same(i, X[i]))
        {
            uf.unite(i, X[i]);
            continue;
        }
        // 嫌っている相手と同じ閉路に所属している。→ 閉路内で最も少ない不満度を足していく
        auto v = i;
        ll cur = 1e10;
        do
        {
            cur = min(C[v], cur);
            v = X[v];
        } while (v != i);
        ans += cur;
    }
    cout << ans << endl;
}