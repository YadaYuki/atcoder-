#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    vector<int> B(N);
    for (int i = 1; i < N; i++)
    {
        cin >> A[i];
    }
    for (int i = 1; i < N; i++)
    {
        cin >> B[i];
    }
    vector<int> dp(N + 1);
    dp.assign(N + 1, -1e9);
    dp[1] = 0;
    for (int i = 1; i < N; i++)
    {
        dp[A[i]] = max(dp[i] + 100, dp[A[i]]);
        dp[B[i]] = max(dp[i] + 150, dp[B[i]]);
    }

    cout << dp[N] << endl;
}