#include <bits/stdc++.h>
#define ll long long
#define MOD 998244353
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<ll> a(N);
    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
    }
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
                    dp[j + 1][k][l] = (dp[j][k][l] + dp[j + 1][k][l]) % MOD;
                    if (k < i)
                    {
                        dp[j + 1][k + 1][(l + a[j]) % i] = (dp[j][k][l] + dp[j + 1][k + 1][(l + a[j]) % i]) % MOD;
                    }
                }
            }
        }
        ans = (ans + dp[N][i][0]) % MOD;
    }
    cout << ans << endl;
}