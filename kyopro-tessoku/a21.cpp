#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> P(N);
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> P[i] >> A[i];
    }
    vector<vector<int>> dp(N + 1, vector<int>(N + 1));

    for (int i = 1; i < N; i++)
    {
        for (int j = N; j > i; j--)
        {
            // iを消す.
            auto pi = P[i - 1];
            int score = 0;
            if (i + 1 <= pi && pi <= j)
            {
                score = A[i - 1];
            }
            dp[i + 1][j] = max(dp[i][j] + score, dp[i + 1][j]);
            // jを消す
            auto pj = P[j - 1];
            score = 0;
            if (i <= pj && pj <= j - 1)
            {
                score = A[j - 1];
            }
            dp[i][j - 1] = max(dp[i][j] + score, dp[i][j - 1]);
            // cout << dp[i][j] << endl;
            // cout << i << "," << j << "," << i + 1 << "," << j << "," << i << "," << j - 1 << endl;
        }
    }
    int ans = -1;
    for (int i = 1; i <= N; i++)
    {
        ans = max(ans, dp[i][i]);
        // cout << dp[i][i] << endl;
    }
    cout << ans << endl;
}