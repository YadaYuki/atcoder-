// 最短距離という意味でBFSの方が解きやすいかも
#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M;
    vector<vector<ll>> graph;
    vector<ll> visited;
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
        //
        queue<ll> q;
        map<ll, ll> distance_from_x;
        distance_from_x[x] = 0;
        vector<ll> connected;
        q.push(x);
        while (q.size() != 0)
        {
            auto cur = q.front();
            q.pop();
            connected.push_back(cur);
            if (distance_from_x[cur] == k)
            {
                continue;
            }
            for (auto next : graph[cur])
            {
                if (distance_from_x.count(next) == 0)
                { // not visited
                    q.push(next);
                    distance_from_x[next] = distance_from_x[cur] + 1;
                }
            }
        }
        for (auto c : connected)
        {
            ans[i] += (c + 1);
        }
    }
    for (auto a : ans)
    {
        cout << a << endl;
    }
}
