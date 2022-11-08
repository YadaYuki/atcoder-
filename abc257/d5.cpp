#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<pair<ll, ll>> jumps(N);
    vector<ll> P(N);

    for (int i = 0; i < N; i++)
    {
        ll x, y, p;
        cin >> x >> y >> p;
        jumps[i] = pair{x, y};
        P[i] = p;
    }

    // calculate practice count
    ll ng = -1;
    ll ok = 5e9;

    while (ok - ng > 1)
    {
        ll mid = (ok + ng) / 2;
        ll s = mid;
        // cout << mid << endl;
        // create directed graph
        vector<vector<int>> Graph(N);
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (i == j)
                    continue;

                auto jump_i = jumps[i];
                auto jump_j = jumps[j];
                auto pi = P[i];
                auto xi = jump_i.first;
                auto yi = jump_i.second;
                auto xj = jump_j.first;
                auto yj = jump_j.second;

                // iからjにjumpできるかどうか
                if (pi * s >= (abs(xi - xj) + abs(yi - yj)))
                {
                    Graph[i].push_back(j);
                }
            }
        }
        bool all_nodes_can_go = false;
        // BFS
        for (int i = 0; i < N; i++)
        {

            vector<bool> visited(N);
            queue<ll> q;
            q.push(i);
            visited[i] = true;
            while (!q.empty())
            {
                auto cur = q.front();
                q.pop();
                for (auto next : Graph[cur])
                {
                    if (!visited[next])
                    {
                        q.push(next);
                        visited[next] = true;
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
            ok = mid;
        }
        else
        {
            ng = mid;
        }
    }
    cout << ok << endl;
}