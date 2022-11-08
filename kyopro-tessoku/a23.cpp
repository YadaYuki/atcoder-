#include <bits/stdc++.h>
#include <cmath>
#define ll long long
using namespace std;

int main()
{

    int N, M;
    cin >> N >> M;
    vector<vector<int>> A(M, vector<int>(N));
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> A[i][j];
        }
        //
    }

    auto pow_N = pow(2, N);
    vector<vector<int>> dp(M + 1, vector<int>(pow_N));

    for (int i = 0; i <= M; i++)
    {
        for (int j = 0; j <= pow_N; j++)
        {
            dp[i][j] = 1e9;
        }
    }

    dp[0][0] = 0;
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < pow_N; j++)
        {
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j]);
            // クーポンiで購入できる商品リストを2進数に変換する.
            auto a = A[i];
            int score = 0;
            for (int k = 0; k < N; k++)
            {
                if (a[k] == 1)
                {
                    score += 1 << k;
                }
            }
            dp[i + 1][j | score] = min(dp[i][j] + 1, dp[i + 1][j | score]);
        }
    }
    // for (int i = 0; i <= M; i++)
    // {
    //     for (int j = 0; j < pow_N; j++)
    //     {
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    int ans = 1e9;
    for (int i = 0; i <= M; i++)
    {
        ans = min(dp[i][pow_N - 1], ans);
    }
    if(ans==1e9){
        ans = -1;
    }
    cout << ans << endl;
}