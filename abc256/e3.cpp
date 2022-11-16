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
    vector<ll> X(N+1);
    vector<ll> C(N+1);

    for (int i = 1; i <= N; i++)
    {
        cin >> X[i];
    }

    for (int i = 1; i <= N; i++)
    {
        cin >> C[i];
    }


    auto uf = UnionFind(N+1);
    ll ans = 0;
    for(int i=1;i<=N;i++){
        if(!uf.is_same(i,X[i])){
            uf.unite(i,X[i]);
            continue;
        }
        auto c = i;
        ll frustration = 1e9 + 1;
        do{
            frustration = min(C[c],frustration);
            c = X[c];
        }while(c!=i);
        ans += frustration;
    }

    cout << ans << endl;

}