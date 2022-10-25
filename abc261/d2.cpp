#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<ll> X(N);
    for (int i = 0; i < N; i++)
    {
        cin >> X[i];
    }
    vector<ll> bonus(N + 1);
    for (int i = 0; i < M; i++)
    {
        ll c, x;
        cin >> c >> x;
        bonus[c] = x;
    }

    vector<vector<ll>> dp(N + 1, vector<ll>(N + 1, 0));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            // 表が出た時
            dp[i + 1][j + 1] = max(dp[i][j] + bonus[j + 1] + X[i], dp[i][j]);
            // 裏が出た時
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][j]);
        }
    }

    ll ans = -1;
    for (int i = 0; i <= N; i++){
        ans = max(dp[N][i],ans);
    }
    cout << ans << endl;

}