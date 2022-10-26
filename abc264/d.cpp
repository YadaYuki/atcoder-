#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    string S;
    cin >> S;
    // BFS
    string Goal = "atcoder";
    map<string, int> costs;
    map<string, bool> visited;
    queue<string> q;
    q.push(S);
    costs[S] = 0;
    visited[S] = true;
    while (!q.empty())
    {
        auto cur = q.front();
        if (cur == "atcoder")
        {
            break;
        }
        q.pop();

        for (int i = 0; i < 6; i++)
        {
            auto next = cur;
            swap(next[i], next[i + 1]);
            if (!visited[next])
            {
                costs[next] = costs[cur] + 1;
                q.push(next);
                visited[next] = true;
            }
        }
    }
    cout << costs["atcoder"] << endl;
}