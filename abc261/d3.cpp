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
    vector<ll> bonus(N + 1, 0);
    for (int i = 0; i < M; i++)
    {
        ll c, y;
        cin >> c >> y;
        bonus[c] = y;
    }

    vector<vector<ll>> dp(N + 1, vector<ll>(N + 1));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            dp[i+1][j+1] = max(dp[i][j] + X[i] + bonus[j+1],dp[i+1][j+1]);  // i回目に表が出た時
            dp[i+1][0] = max(dp[i][j],dp[i+1][0]);
        }
    }
    ll ans = -1;
    for(int i=0;i<N+1;i++){
        ans = max(ans,dp[N][i]);
    }
    cout << ans << endl;
}