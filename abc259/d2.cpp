#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    int sx, sy, tx, ty;
    cin >> sx >> sy >> tx >> ty;
    vector<vector<ll>> circles(N, vector<ll>(3));
    for (int i = 0; i < N; i++)
    {
        int x, y, r;
        cin >> x >> y >> r;
        circles[i][0] = x;
        circles[i][1] = y;
        circles[i][2] = r;
    }
    int s, t;
    for (int i = 0; i < N; i++)
    {
        auto ci = circles[i];
        auto x = ci[0];
        auto y = ci[1];
        auto r = ci[2];
        ll ds = (sx - x) * (sx - x) + (sy - y) * (sy - y);
        if (ds == r * r)
        {
            s = i;
        }
        ll dt = (tx - x) * (tx - x) + (ty - y) * (ty - y);
        if (dt == r * r)
        {
            t = i;
        }
    }

    vector<vector<int>> Graph(N);
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            auto ci = circles[i];
            auto cj = circles[j];
            auto xi = ci[0];
            auto yi = ci[1];
            auto ri = ci[2];
            auto xj = cj[0];
            auto yj = cj[1];
            auto rj = cj[2];
            ll d = (xi - xj) * (xi - xj) + (yi - yj) * (yi - yj);
            bool is_connected = (ri - rj) * (ri - rj) <= d && d <= (ri + rj) * (ri + rj);
            if (is_connected)
            {
                Graph[i].push_back(j);
                Graph[j].push_back(i);
            }
        }
    }
    // BFS
    queue<int> q;
    q.push(s);
    vector<bool> visited;
    visited.assign(N,false);
    visited[s] = true;
    while(!q.empty() && !visited[t]){
        auto cur = q.front();
        q.pop();
        for(auto next:Graph[cur]){
            if(!visited[next]){
                q.push(next);
                visited[next] = true;
            }
        }
    }
    if(visited[t]) {
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}