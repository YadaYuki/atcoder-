#include <bits/stdc++.h>
using namespace std;
#define BIG 1000000000

struct Edge
{
    int to, cap, rev;
}; // 2部マッチング問題なのでcapは不要 は ウソ。 //

class MaximumFlow
{

private:
    int size;
    vector<vector<Edge>> graph;
    vector<bool> visited;

    int dfs(int cur, int goal, int flow_to_cur)
    {
        visited[cur] = true;
        if (cur == goal)
        {
            return flow_to_cur;
        }
        for (unsigned long i = 0; i < graph[cur].size(); i++)
        {
            auto next_edge = graph[cur][i];
            if (visited[next_edge.to])
            {
                continue;
            }
            if (next_edge.cap == 0)
            {
                continue;
            }
            auto flow_to_goal = dfs(next_edge.to, goal, min(flow_to_cur, next_edge.cap));
            if (flow_to_goal > 0)
            {
                graph[cur][i].cap -= flow_to_goal;
                graph[next_edge.to][next_edge.rev].cap += flow_to_goal;
                return flow_to_goal;
            }
        }
        return 0;
    }

public:
    explicit MaximumFlow(int N)
    {
        size = N;
        graph.assign(N, vector<Edge>());
        visited.assign(N, false);
    }

    void add_edge(int a, int b, int cap)
    {
        // add edge between node a & node b.
        int edges_num_from_a = graph[a].size();
        int edges_num_from_b = graph[b].size();
        graph[a].push_back(Edge{b, cap, edges_num_from_b});
        graph[b].push_back(Edge{a, 0, edges_num_from_a});
    }

    int maximum_flow(int start, int goal)
    {
        int total_flow = 0;
        bool way_to_goal_exist = true;
        while (way_to_goal_exist)
        {
            for (int i = 0; i < size; i++)
            {
                visited[i] = false;
            }
            auto flow_to_goal = dfs(start, goal, BIG);
            total_flow += flow_to_goal;
            way_to_goal_exist = (flow_to_goal > 0);
        }
        return total_flow;
    }
};

int main()
{
    int N;
    cin >> N;
    int nodes_num = N + N + 2; // students + seats + start & goal
    auto mf = MaximumFlow(nodes_num);
    for (int student = 0; student < N; student++)
    {
        string s;
        cin >> s;
        for (int i = 0; i < N; i++)
        {
            if (s.at(i) == '#')
            {
                int seat = i + N;
                mf.add_edge(student,seat,1);
            }
        }
    }

    int start = 2 * N;
    int goal = 2 * N + 1;
    
    // add edges from start to all students.
    for(int student = 0; student < N; student++){
        mf.add_edge(start,student,1);
    }

    // add edges from all seats to goal.
    for(int i = 0; i < N; i++){
        int seat = i + N;
        mf.add_edge(seat,goal,1);
    }

    cout << mf.maximum_flow(start,goal) << endl;

}