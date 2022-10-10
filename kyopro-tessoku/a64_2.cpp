#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<long long, long long> > > weighted_graph;
vector<long long> cost_to_nodes;

int main()
{
    int N, M;
    cin >> N >> M;
    weighted_graph.assign(N, vector<pair<long long, long long> >());
    cost_to_nodes.assign(N, -1);
    for (int i = 0; i < M; i++)
    {
        int A, B, C;
        cin >> A >> B >> C;
        A--;
        B--;
        weighted_graph[A].push_back(pair<long long, long long>(C, B));
        weighted_graph[B].push_back(pair<long long, long long>(C, A));
    }
    priority_queue<pair<long long, long long> > pq;
    pq.push(pair<long long, long long>(0, 0));
    cost_to_nodes[0] = 0;
    while (!pq.empty())
    {
        auto c = pq.top();
        pq.pop();
        for (auto next : weighted_graph[c.second])
        {
            auto not_visited = cost_to_nodes[next.second] == -1;
            if (not_visited)
            {
                cost_to_nodes[next.second] = cost_to_nodes[c.second] + next.first;
                pq.push(next);
            }
            else if (cost_to_nodes[next.second] > cost_to_nodes[c.second] + next.first)
            {
                cost_to_nodes[next.second] = cost_to_nodes[c.second] + next.first;
                pq.push(next); // ここでもう一度再探索の候補になるのか...。
            }
        }
    }
    for(auto cost:cost_to_nodes){
        cout << cost << endl;
    }
}