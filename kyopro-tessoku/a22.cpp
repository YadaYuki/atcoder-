#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<ll> A(N);
    vector<ll> B(N);
    for (int i = 1; i <= N-1; i++)
    {
        cin >> A[i];
    }
    for (int i = 1; i <= N-1; i++)
    {
        cin >> B[i];
    }
    vector<ll> dp(N + 1);
    // // 配列の初期化
    dp[1] = 0;
    for (int i = 2; i <= N; i++)
        dp[i] = -100000000;

    for (int i = 1; i <= N - 1; i++)
    {
        dp[A[i]] = max(dp[i] + 100, dp[A[i]]);
        dp[B[i]] = max(dp[i] + 150, dp[B[i]]);
    }
    cout << dp[N] << endl;
}