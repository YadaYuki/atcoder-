#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll N, M;
vector<ll> A;
vector<vector<ll>> graph;

bool is_x_ok(ll x)
{
    vector<ll> costs_to_remove(N, 0);
    vector<ll> removed(N, false);
    stack<ll> removal_nodes;
    for (ll i = 0; i < N; i++)
    {
        for (auto n : graph[i])
        {
            costs_to_remove[i] += A[n];
        }
        if (costs_to_remove[i] <= x)
        {
            removal_nodes.push(i);
            removed[i] = true;
        }
    }

    while (!removal_nodes.empty())
    {
        auto cur = removal_nodes.top();
        removal_nodes.pop(); // removed cur
        removed[cur] = true;
        for (auto next : graph[cur])
        {
            if (!removed[next])
            {
                costs_to_remove[next] -= A[cur];
                if (costs_to_remove[next] <= x)
                {
                    removal_nodes.push(next);
                }
            }
        }
    }

    for (auto r : removed)
    {
        if (!r)
        {
            return false;
        }
    }

    return true;
}


int main()
{
    cin >> N >> M;
    A.assign(N, 0);
    for (ll i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    graph.assign(N, vector<ll>());
    for (ll i = 0; i < M; i++)
    {
        ll u, v;
        cin >> u >> v;
        u--;
        v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    ll A_max = *max_element(A.begin(), A.end());
    ll ok = A_max * N + 1;
    ll ng = -1;
    while (ok - ng > 1)
    {
        ll mid = (ok + ng) / 2;
        auto mid_is_ok = is_x_ok(mid);
        if (mid_is_ok)
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
