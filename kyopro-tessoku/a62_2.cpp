#include <bits/stdc++.h>
using namespace std;

vector<vector<long long> > Graph;
vector<bool> visited;

void dfs(int prev, int cur)
{
    visited[cur] = true;
    for (auto next : Graph[cur])
    {
        auto is_visited = visited[next];
        if (!is_visited && prev != next)
            dfs(cur, next);
    }
}

int main()
{
    int N, M;
    cin >> N >> M;
    Graph.assign(N, vector<long long>());
    visited.assign(N, false);

    for (int i = 0; i < M; i++)
    {
        int A, B;
        cin >> A >> B;
        A--;
        B--;
        Graph[A].push_back(B);
        Graph[B].push_back(A);
    }
    dfs(-1,0);
    for(auto v:visited){
        if(!v){
            cout << "The graph is not connected." << endl;
            exit(0);
        }
    }
    cout << "The graph is connected." << endl;
}