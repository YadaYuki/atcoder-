#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N, M;
    cin >> N >> M;
    vector<ll> A(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    vector<vector<ll>> graph(N);
    for (ll i = 0; i < M; i++)
    {
        ll u, v;
        cin >> u >> v;
        u--;
        v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    auto max_A = max_element(A.begin(), A.end());
    ll ok = (*max_A) * M + 1;
    ll ng = -1LL;
    while (ok - ng > 1)
    {
        ll mid = (ok + ng) / 2;
        // check whether all nodes can remove under cost of "mid".
        vector<ll> costs_to_remove(N, 0);
        vector<bool> removed(N, false);
        stack<ll> q;
        for (ll i = 0; i < N; i++)
        {
            for (auto n : graph[i])
            {
                costs_to_remove[i] += A[n];
            }
            if (mid >= costs_to_remove[i])
            {
                q.push(i);
                removed[i] = true;
            }
        }
        while (!q.empty())
        {
            auto c = q.top();
            q.pop();
            for (auto n : graph[c])
            {
                if (removed[n])
                    continue;
                costs_to_remove[n] -= A[c];
                if (mid >= costs_to_remove[n])
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
    cout  << ok << endl;
}