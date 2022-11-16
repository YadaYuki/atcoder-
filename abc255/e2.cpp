#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<ll> S(N - 1);
    vector<ll> X(M);
    vector<ll> B(N);

    for (int i = 0; i < N - 1; i++)
    {
        cin >> S[i];
    }

    for (int i = 0; i < M; i++)
    {
        cin >> X[i];
    }

    for (int i = 1; i < N; i++)
    {
        B[i] = S[i - 1] - B[i - 1];
    }

    map<ll, ll> A_first_candidates;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            auto A_first = X[j] - B[i];
            if (i % 2 == 1)
            {
                A_first *= -1;
            }
            A_first_candidates[A_first] += 1;
        }
    }
    ll ans = -1;
    for (auto [k, v] : A_first_candidates)
    {
        ans = max(ans, v);
    }
    cout << ans << endl;
}