#include <bits/stdc++.h>
#include <cmath>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    ll sx, sy, tx, ty;
    cin >> sx >> sy >> tx >> ty;
    vector<vector<ll>> Circles(N);
    for (int i = 0; i < N; i++)
    {
        ll x, y, r;
        cin >> x >> y >> r;
        Circles[i].push_back(x);
        Circles[i].push_back(y);
        Circles[i].push_back(r);
    }

    // calculate start circle & end circle;

    int s = -1;
    int t = -1;
    for (int i = 0; i < N; i++)
    {
        auto ci = Circles[i];
        auto xi = ci[0];
        auto yi = ci[1];
        auto ri = ci[2];
        double distance_s = sqrt(pow(xi - sx, 2) + pow(yi - sy, 2));
        if (distance_s == double(ri))
        {
            s = i;
        }
        double distance_t = sqrt(pow(xi - tx, 2) + pow(yi - ty, 2));
        if (distance_t == double(ri))
        {
            t = i;
        }
    }

    // cout << s << ", " << t << endl;

    // Create Graph
    vector<vector<int>> Graph(N);
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            auto ci = Circles[i];
            auto cj = Circles[j];
            // Check whether ci & cj are connected.
            auto xi = ci[0];
            auto yi = ci[1];
            auto ri = ci[2];
            auto xj = cj[0];
            auto yj = cj[1];
            auto rj = cj[2];
            // ll distance_between_centers = pow(xi - xj, 2) + pow(yi - yj, 2);
            ll distance_between_centers = (xi - xj) * (xi - xj) + (yi - yj) * (yi - yj);
            bool is_connected = !(distance_between_centers > (ri+rj)*(ri+rj) || distance_between_centers < (ri-rj)*(ri-rj));
            // cout << is_connected << endl;
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
    vector<bool> visited(N);
    visited[s] = true;
    while (!q.empty() && !visited[t])
    {
        auto cur = q.front();
        q.pop();
        for (auto next : Graph[cur])
        {
            if (!visited[next])
            {
                q.push(next);
                visited[next] = true;
            }
        }
    }
    if (visited[t])
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
}