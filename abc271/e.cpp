#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M, K;
    cin >> N >> M >> K;
    vector<ll> A(M), B(M), C(M);
    for (int i = 0; i < M; i++)
    {
        cin >> A[i] >> B[i] >> C[i];
        A[i]--;
        B[i]--;
    }
    vector<ll> E(K);
    for (int i = 0; i < K; i++)
    {
        cin >> E[i];
        E[i]--;
    }
    ll BIG = 100000000000000000;
    vector<ll> dp(N, BIG);
    dp[0] = 0;
    for (auto e : E)
    {
        dp[B[e]] = min(dp[B[e]], dp[A[e]] + C[e]);
    }
    if (dp[N - 1] == BIG)
    {
        cout << -1 << endl;
    }
    else
    {
        cout << dp[N - 1] << endl;
    }
}