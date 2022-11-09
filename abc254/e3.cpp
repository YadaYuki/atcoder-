#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<vector<int>> graph(N);
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
    vector<int> ans(Q, 0);
    for (int i = 0; i < Q; i++)
    {
        int x, k;
        cin >> x >> k;
        x--;
        // BFS
        queue<int> q;
        map<int, int> distance_from_x;
        q.push(x);
        distance_from_x[x] = 0;
        while (q.size() > 0)
        {
            auto cur = q.front();
            q.pop();
            if (distance_from_x[cur] == k)
            {
                continue;
            }
            for (auto n : graph[cur])
            {
                auto visited = (distance_from_x.count(n) != 0);
                if (!visited)
                {
                    distance_from_x[n] = distance_from_x[cur] + 1;
                    q.push(n);
                }
            }
        }

        for (const auto &[key, value] : distance_from_x)
        {
            ans[i] += (key + 1);
        }
    }
    for(auto a:ans){
        cout << a << endl;
    }
}