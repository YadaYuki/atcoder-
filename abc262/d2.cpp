#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    ll MOD = 998244353;
    vector<ll> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    //
    //
    ll ans = 0;
    for (int i = 1; i <= N; i++)
    {
        vector dp(N + 1, vector(i + 1, vector<ll>(i, 0)));
        dp[0][0][0] = 1;
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k <= i; k++)
            {
                for (int l = 0; l < i; l++)
                {
                    dp[j + 1][k][l] = (dp[j + 1][k][l] + dp[j][k][l]) % MOD;
                    if (i > k)
                    {
                        dp[j + 1][k + 1][(A[j] + l) % i] = (dp[j + 1][k + 1][(A[j] + l) % i] + dp[j][k][l]) % MOD;
                    }
                }
            }
        }
        ans = (ans + dp[N][i][0]) % MOD;
    }
    cout << ans << endl;
}