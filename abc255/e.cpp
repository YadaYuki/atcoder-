#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<ll> S(N - 1);
    vector<ll> X(M);
    for (int i = 0; i < N - 1; i++)
    {
        cin >> S[i];
    }
    for (int i = 0; i < M; i++)
    {
        cin >> X[i];
    }
    vector<ll> B(N);
    B[0] = 0;
    for (int i = 1; i < N; i++)
    {
        B[i] = S[i - 1] - B[i - 1];
    }

    map<ll, ll> m;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            auto z = X[j] - B[i];
            if (i % 2 == 1)
            {
                z *= -1;
            }
            m[z] += 1;
        }
    }
    auto iter = m.begin();
    ll ans = -1;
    while (iter != m.end())
    {
        ans = max(ans, iter->second);
        ++iter;
    }
    cout << ans << endl;
}