#include <bits/stdc++.h>
using namespace std;

struct Edge
{
    int to, cap, rev;
};

class MaximumFlow
{
private:
    vector<vector<Edge>> graph;
    int _size;
    vector<bool> visited;
    int dfs(int cur, int goal, int flow_to_cur)
    {
        if (cur == goal)
        {
            return flow_to_cur;
        }
        visited[cur] = true;
        for (unsigned long i = 0; i < graph[cur].size(); i++)
        {
            auto edge_to_next = graph[cur][i];
            if (edge_to_next.cap == 0)
            {
                continue;
            }
            if (visited[edge_to_next.to])
            {
                continue;
            }
            auto flow_to_goal = dfs(edge_to_next.to, goal, min(flow_to_cur, edge_to_next.cap));
            if (flow_to_goal > 0)
            {
                graph[cur][i].cap -= flow_to_goal;
                graph[edge_to_next.to][edge_to_next.rev].cap += flow_to_goal;
                return flow_to_goal;
            }
        }
        return 0;
    }

public:
    explicit MaximumFlow(int size)
    {
        _size = size;
        graph.assign(size, vector<Edge>());
        visited.assign(size, false);
    }

    void add_edge(int a, int b, int cap)
    {
        // add edge from a to b;
        int edge_cnt_from_a = graph[a].size();
        int edge_cnt_from_b = graph[b].size();
        graph[a].push_back(Edge{b, cap, edge_cnt_from_b});
        graph[b].push_back(Edge{a, 0, edge_cnt_from_a});
    }

    int maximum_flow(int start, int goal)
    {
        int total_flow = 0;
        auto way_to_goal_exists = true;
        while (way_to_goal_exists)
        {
            for (int i = 0; i < _size; i++)
            {
                visited[i] = false;
            }
            auto flow = dfs(start, goal, 100000000);
            way_to_goal_exists = flow > 0;
            total_flow += flow;
        }
        return total_flow;
    }
};

int main()
{
    int N;
    cin >> N;
    auto node_num = N + N + 2; // students + seats + start & goal.
    auto mf = MaximumFlow(node_num);
    for (int student = 0; student < N; student++)
    {
        string s;
        cin >> s;
        for (int i = 0; i < N; i++)
        {
            if (s.at(i) == '#')
            {
                int seat = i + N;
                mf.add_edge(student, seat, 1);
            }
        }
    }
    int start = 2 * N;
    int goal = 2 * N + 1;

    // add edge from start to students.
    for (int student = 0; student < N; student++)
    {
        mf.add_edge(start, student, 1);
    }

    // add edge from seats to goal.
    for (int seat = N; seat < 2 * N; seat++)
    {
        mf.add_edge(seat, goal, 1);
    }

    cout << mf.maximum_flow(start, goal) << endl;
}