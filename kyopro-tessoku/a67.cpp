#include <bits/stdc++.h>

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
    int N, M;
    cin >> N >> M;
    auto uf = UnionFind(N+100);
    vector<pair<int,pair<int,int> > > edges;
    for (int i = 0; i < M; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        auto edge = make_pair(a,b);
        auto weighted_edge = make_pair(c,edge);
        edges.push_back(weighted_edge);
    }
    // https://cpprefjp.github.io/reference/algorithm/sort.html
    sort(edges.begin(), edges.end());
    int ans = 0;
    for (auto edge : edges)
    {
        if (!uf.is_same(edge.second.first, edge.second.second))
        {
            uf.unite(edge.second.first, edge.second.second);
            ans += edge.first;
        }
    }
    cout << ans << endl;
}