#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long N, M;
    priority_queue<pair<long long, long long> > pq;
    vector<vector<pair<long long, long long> > > G;
    vector<long long> costs_to_nodes;
    cin >> N >> M;
    G.assign(N, vector<pair<long long, long long> >());
    costs_to_nodes.assign(N, -1);
    for (int i = 0; i < M; ++i)
    {
        long long A, B, C;
        cin >> A >> B >> C;
        A--;
        B--;
        G[A].push_back(make_pair(C, B));
        G[B].push_back(make_pair(C, A));
    }

    costs_to_nodes[0] = 0L;
    pq.push(make_pair(0, 0));

    while (!pq.empty())
    {
        auto cur = pq.top();
        pq.pop();
        // auto cur_cost = cur.first;
        auto cur_node = cur.second;
        for (auto next : G[cur_node])
        {
            auto next_cost = next.first;
            auto next_node = next.second;
            auto visited = (costs_to_nodes[next_node] != -1);
            if (!visited)
            {
                costs_to_nodes[next_node] = costs_to_nodes[cur_node] + next_cost;
                pq.push(next);
            }
            if(costs_to_nodes[next_node] > (costs_to_nodes[cur_node] + next_cost))
            {
                costs_to_nodes[next_node] = costs_to_nodes[cur_node] + next_cost;
                pq.push(next);
            }
        }
    }

    for (long long i = 0; i < N; i++)
    {
        cout << costs_to_nodes[i] << endl;
    }
}