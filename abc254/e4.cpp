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
    vector<int> ans(Q);
    for (int i = 0; i < Q; i++)
    {
        int x, k;
        cin >> x >> k;
        x--;
        int q_ans = 0;
        map<int, int> costs;
        queue<int> q;
        costs[x] = 0;
        q.push(x);
        q_ans += x + 1;
        while (!q.empty())
        {
            auto cur = q.front();
            q.pop();
            for (auto next : graph[cur])
            {
                auto visited = costs.count(next) != 0;
                if (!visited)
                {
                    auto cost_to_next = costs[cur] + 1;
                    costs[next] = cost_to_next;
                    if (cost_to_next <= k)
                    {
                        q_ans += next + 1;
                        q.push(next);
                    }
                }
            }
        }
        ans[i] = q_ans;
    }
    for (auto a : ans)
    {
        cout << a << endl;
    }
}