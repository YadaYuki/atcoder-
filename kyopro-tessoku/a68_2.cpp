#include <bits/stdc++.h>
using namespace std;

struct Edge
{
    int to, cap, rev;
};

class MaximumFlow
{
private:
    vector<vector<Edge>> directed_graph;
    vector<bool> visited;

public:
    explicit MaximumFlow(int size)
    {
        directed_graph.assign(size, vector<Edge>());
        visited.assign(size, false);
    }

    void add_edge(int from, int to, int cap)
    {
        int edge_cnt_from = directed_graph[from].size();
        int edge_cnt_to = directed_graph[to].size();
        directed_graph[from].push_back(Edge{to, cap, edge_cnt_to});
        directed_graph[to].push_back(Edge{from, 0, edge_cnt_from});
    }

    int dfs(int cur, int goal, int flow_to_cur)
    {
        if (cur == goal)
        {
            return flow_to_cur;
        }
        visited[cur] = true;
        for (unsigned long i = 0; i < directed_graph[cur].size(); i++)
        {
            auto next = directed_graph[cur][i];
            if (visited[next.to])
            {
                continue;
            }
            if (next.cap == 0)
            {
                continue;
            }
            auto maximum_flow_to_goal = dfs(next.to, goal, min(flow_to_cur, next.cap));
            if (maximum_flow_to_goal > 0)
            {
                directed_graph[cur][i].cap -= maximum_flow_to_goal;
                directed_graph[next.to][next.rev].cap += maximum_flow_to_goal;
                return maximum_flow_to_goal;
            }
        }
        return 0;
    }

    int maximum_flow(int start, int goal)
    {
        int total_flow = 0;
        bool has_way = true;
        while (has_way)
        {
            for (unsigned long i = 0; i < visited.size(); i++)
            {
                visited[i] = false;
            }
            auto flow = dfs(start, goal, 1000000000);
            total_flow += flow;
            has_way = flow > 0;
        }
        return total_flow;
    }
};

int main()
{
    int N, M;
    cin >> N >> M;
    auto mf = MaximumFlow(N);
    for (int i = 0; i < M; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        mf.add_edge(a, b, c);
        // cout << a << b << c << endl;
    }
    cout << mf.maximum_flow(0, N - 1) << endl;
}
