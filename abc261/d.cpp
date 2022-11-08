#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<ll> X;
    for (int i = 0; i < N; i++)
    {
        int x;
        cin >> x;
        X.push_back(x);
    }
    vector<ll> bonus;
    bonus.assign(N + 1, 0);

    for (int i = 0; i < M; i++)
    {
        int c, y;
        cin >> c >> y;
        bonus[c] = y;
    }

    vector<vector<ll>> dp(N + 1, vector<ll>(N + 1));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + bonus[j + 1] + X[i]);
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][j]);
        }
    }
    // for (int i = 0; i < N + 1; i++)
    // {
    //     for (int j = 0; j < N + 1; j++)
    //     {
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    ll ans = -1;
    for (int i = 0; i < N + 1; i++)
    {
        ans = max(dp[N][i], ans);
    }
    cout << ans << endl;
}