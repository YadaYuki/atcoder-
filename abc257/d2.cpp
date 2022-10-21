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
    // int s;
    // cin >> s;
    ll s_ok = 1e10;
    ll s_ng = -1;
    while (s_ok - s_ng > 1)
    {
        auto s = (s_ok + s_ng) / 2;
        // cout << s << endl;
        vector<vector<ll>> graph(N);
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
                        // cout << i << ", " << j << endl;
                    }
                }
            }
        }
        bool all_nodes_can_go = true;
        for (int i = 0; i < N; i++)
        {
            all_nodes_can_go = true;
            for (int j = 0; j < N; j++)
            {
                // bfs
                if (i == j)
                {
                    continue;
                }
                queue q = queue<ll>();
                q.push(i);
                vector<bool> visited;
                visited.assign(N, false);
                bool can_go_from_i_to_j = false;
                while (!q.empty() && !can_go_from_i_to_j)
                {
                    auto c = q.front();
                    q.pop();
                    visited[c] = true;
                    for (auto next : graph[c])
                    {
                        if (!visited[next])
                        {
                            q.push(next);
                            can_go_from_i_to_j = can_go_from_i_to_j || (next == j);
                            // cout << i << ", " << j << (can_go_from_i_to_j ? "ok" : "ng") << endl;
                        }
                    }
                }
                all_nodes_can_go = all_nodes_can_go && can_go_from_i_to_j;
                if (!all_nodes_can_go)
                {
                    break;
                }
            }
            if (all_nodes_can_go)
            {
                break;
            }
        }
        // cout << s << ": " << (all_nodes_can_go ? "Yes" : "No") << endl;
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