#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long N, M;
    queue<long long> Q;
    vector<vector<long long> > G;
    vector<long long> costs_to_nodes;
    cin >> N >> M;
    G.assign(N, vector<long long>());
    costs_to_nodes.assign(N, -1);
    for (int i = 0; i < M; ++i)
    {
        long long A, B;
        cin >> A >> B;
        A--;
        B--;
        G[A].push_back(B);
        G[B].push_back(A);
    }

    Q.push(0L);
    costs_to_nodes[0] = 0;

    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        for (auto next : G[cur])
        {
            bool visited = (costs_to_nodes[next] != -1);
            if (!visited)
            {
                costs_to_nodes[next] = costs_to_nodes[cur] + 1;
                Q.push(next);
            }
        }
    }

    for (long long i = 0; i < N; i++)
    {
        cout << costs_to_nodes[i] << endl;
    }
}