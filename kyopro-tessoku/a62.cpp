#include <bits/stdc++.h>
using namespace std;
#define MAX_VAL 100009

vector<vector<long long> > G;
stack<long long> st;
vector<bool> visited;

void dfs(long long prev, long long cur)
{
    visited[cur] = true;
    for (auto next : G[cur])
    {
        if ((!visited[next]) && (prev != next))
        {
            dfs(cur, next);
        }
    }
}

int main()
{
    long long N, M;
    cin >> N >> M;
    G.assign(N, vector<long long>());
    visited.assign(N, false);
    for (int i = 0; i < M; ++i)
    {
        long long A, B;
        cin >> A >> B;
        A--;
        B--;
        G[A].push_back(B);
        G[B].push_back(A);
    }
    dfs(-1, 0);
    for (int i = 0; i < N; i++)
    {
        if (visited[i] != true)
        {
            cout << "The graph is not connected." << endl;
            exit(0);
        }
    }
    cout << "The graph is connected." << endl;
}