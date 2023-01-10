#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N, M;
    cin >> N >> M;
    vector<ll> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    vector<vector<ll>> graph(N);
    for (int i = 0; i < M; i++)
    {
        ll u, v;
        cin >> u >> v;
        u--;
        v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    // binary search
    ll ok = 10000000000000000;
    ll ng = -1;
    while (ok - ng > 1)
    {
        ll mid = (ok + ng) / 2;
        //
        vector<ll> costs_to_remove(N, 0);
        queue<ll> q;
        vector<bool> removed(N, false);
        for (int i = 0; i < N; i++)
        {
            for (auto n : graph[i])
            {
                costs_to_remove[i] += A[n];
            }
            if (costs_to_remove[i] <= mid)
            {
                q.push(i);
                removed[i] = true;
            }
        }
        while (!q.empty())
        {
            auto cur = q.front();
            q.pop();
            for (auto n : graph[cur])
            {
                if (removed[n])
                {
                    continue;
                }
                costs_to_remove[n] -= A[cur];
                if (costs_to_remove[n] <= mid)
                {
                    q.push(n);
                    removed[n] = true;
                }
            }
        }
        bool is_ok = true;
        for (auto r : removed)
        {
            if (!r)
            {
                is_ok = false;
                break;
            }
        }
        if (is_ok)
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