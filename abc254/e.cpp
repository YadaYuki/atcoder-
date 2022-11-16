#include <bits/stdc++.h>
#define ll long long
using namespace std;

vector<vector<ll>> graph;
vector<ll> visited;

ll dfs(ll prev, ll cur, int distance, int k)
{
    cout << (cur + 1) << "," << distance << endl;
    visited[cur] = true;
    if (distance == k)
    {
        return cur + 1;
    }
    ll total = cur + 1;
    for (auto next : graph[cur])
    {
        if (visited[next])
        {
            continue;
        }
        if (next != prev)
        {
            total += dfs(cur, next, distance + 1, k);
        }
    }
    return total;
}

int main()
{
    int N, M;
    cin >> N >> M;
    graph.assign(N, vector<ll>());
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    int Q;
    cin >> Q;
    vector<ll> ans(Q);
    for (int i = 0; i < Q; i++)
    {
        int x, k;
        cin >> x >> k;
        x--;
        visited.assign(N, false);
        ans[i] = dfs(-1, x, 0, k);
    }
    for (auto a : ans)
    {
        cout << a << endl;
    }
}

