#include <bits/stdc++.h>
using namespace std;

struct Edge
{
    int to, cap, rev;
};

class MaximumFlow
{
private:
    int size;
    vector<vector<Edge> > Graph;
    vector<bool> used;

public:
    explicit MaximumFlow(int N)
    {
        size = N;
        Graph.assign(N, vector<Edge>());
        used.assign(N, false);
    }
    void add_edge(int a, int b, int c)
    {
        int cur_ga = Graph[a].size();
        int cur_gb = Graph[b].size();
        auto a2b = Edge{b, c, cur_gb};
        auto b2a = Edge{a, 0, cur_ga};
        Graph[a].push_back(a2b);
        Graph[b].push_back(b2a);
    }

    int dfs(int pos, int goal, int flow)
    {
        if (pos == goal)
        {
            return flow;
        }
        used[pos] = true;
        for (unsigned i = 0; i < Graph[pos].size(); i++)
        {
            auto edge = Graph[pos][i];
            if (edge.cap == 0)
                continue;
            if (used[edge.to])
                continue;
            int f = dfs(edge.to, goal, min(flow, edge.cap));
            if (f >= 1)
            {
                Graph[pos][i].cap -= f;
                Graph[Graph[pos][i].to][Graph[pos][i].rev].cap += f;
                return f;
            }
        }

        return 0;
    }

    int max_flow(int s, int t)
    {
        int total_flow = 0;
        while (true)
        {
            used.assign(size, false);
            auto f = dfs(s, t, 1000000000);
            if (f == 0)
                break;
            total_flow += f;
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
        int A, B, C;
        cin >> A >> B >> C;
        A--;
        B--;
        mf.add_edge(A, B, C);
    }
    cout << mf.max_flow(0, N - 1) << endl;
}