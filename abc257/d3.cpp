#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<vector<ll>> jump(N);
    for (int i = 0; i < N; i++)
    {
        ll x, y, p;
        cin >> x >> y >> p;
        jump[i].push_back(x);
        jump[i].push_back(y);
        jump[i].push_back(p);
    }
    ll s_ok = 5e9;
    ll s_ng = -1;
    while (s_ok - s_ng > 1)
    {
        auto s = (s_ok + s_ng) / 2;
        vector<vector<int>> graph(N);
        for (int i = 0; i < N; i++)
        {
            auto from = jump[i];
            ll p = from[2];
            for (int j = 0; j < N; j++)
            {
                if (i != j)
                {
                    auto to = jump[j];
                    ll xi = from[0];
                    ll yi = from[1];
                    ll xj = to[0];
                    ll yj = to[1];
                    if (p * s >= (abs(xi - xj) + abs(yi - yj)))
                    {
                        graph[i].push_back(j);
                    }
                }
            }
        }
        bool all_nodes_can_go = false;
        for (int i = 0; i < N; i++)
        {
            queue q = queue<ll>();
            q.push(i);
            vector<bool> visited(N);
            visited[i] = true;
            while (!q.empty())
            {
                auto c = q.front();
                q.pop();
                visited[c] = true;
                for (auto next : graph[c])
                {
                    if (!visited[next])
                    {
                        q.push(next);
                    }
                }
            }
            all_nodes_can_go = true;
            for (auto v : visited)
            {
                if (!v)
                {
                    all_nodes_can_go = false;
                    break;
                }
            }
            if (all_nodes_can_go)
            {
                break;
            }
        }
        if (all_nodes_can_go)
        {
            s_ok = s;
        }
        else
        {
            s_ng = s;
        }
    }
    cout << s_ok << endl;
}