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
    int N, M;
    cin >> N >> M;
    auto uf = UnionFind(N + 1);
    vector<vector<int> > edges;
    for (int i = 0; i < M; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        vector<int> edge;
        edge.push_back(c);
        edge.push_back(a);
        edge.push_back(b);
        edges.push_back(edge);
    }

    sort(edges.begin(), edges.end());

    int total_cost = 0;
    for (auto edge : edges)
    {
        int cost = edge[0];
        int u = edge[1];
        int v = edge[2];
        if(!uf.same(u,v)){
            uf.unite(u,v);
            total_cost += cost;
        }
    }
    cout << total_cost << endl;
}