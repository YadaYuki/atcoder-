#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    vector<int> P(N);
    for (int i = 0; i < N; i++)
    {
        cin >> P[i] >> A[i];
    }
    vector<vector<int>> dp(N + 1, vector<int>(N + 1));
    for (int l = 1; l < N; l++)
    {
        for (int r = N; r > l; r--)
        {
            // remove R
            int score = 0;
            auto pi = P[r - 1];
            if (l <= pi && pi <= r - 1)
            {
                score = A[r - 1];
            }
            dp[l][r - 1] = max(dp[l][r] + score, dp[l][r - 1]);
            // remove L
            score = 0;
            pi = P[l - 1];
            if (l + 1 <= pi && pi <= r)
            {
                score = A[l - 1];
            }
            dp[l + 1][r] = max(dp[l][r] + score, dp[l + 1][r]);
        }
    }
    int ans = -1;
    for(int i=1;i<=N;i++){
        ans = max(dp[i][i],ans);
    }
    cout << ans << endl;
}