#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    string S;
    cin >> S;
    string GOAL = "atcoder";
    //  BFS
    queue<string> q;
    map<string, int> costs;
    map<string, bool> visited;

    visited[S] = true;
    costs[S] = 0;
    q.push(S);

    while ((!q.empty()) && (!visited[GOAL]))
    {
        auto cur = q.front();
        q.pop();
        // cout << cur << endl;

        for (int i = 0; i < 6; i++)
        {
            auto next = cur;
            swap(next[i], next[i + 1]);
            if (!visited[next])
            {
                visited[next] = true;
                costs[next] = costs[cur] + 1;
                q.push(next);
            }
        }
    }
    cout << costs[GOAL] << endl;
}