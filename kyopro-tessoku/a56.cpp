#include <bits/stdc++.h>
using namespace std;

long long pos_to_hash[200001];
long long pos_to_num[200001];
long long MOD = 1000000007;
long long POWER100[200001];

long long calculate_hash(long long r, long long l)
{
    long long hash = pos_to_hash[r] - (pos_to_hash[l - 1] * POWER100[r - l + 1] % MOD);
    if (hash < 0)
    {
        hash += MOD;
    }
    return hash;
}

int main()
{
    long long N, Q;
    string S;
    cin >> N >> Q;
    cin >> S;

    POWER100[0] = 1;
    for (long long i = 1; i <= N; i++)
    {
        POWER100[i] = (POWER100[i - 1] * 100LL) % MOD;
    }

    for (long long i = 1; i <= N; i++)
    {
        pos_to_num[i] = (S[i - 1] - 'a') + 1;
    }
    pos_to_hash[0] = 0;
    for (long long i = 1; i <= N; i++)
    {
        pos_to_hash[i] = (pos_to_num[i] + pos_to_hash[i-1] * 100LL) % MOD;
    }
    for (long long i = 0; i < Q; i++)
    {
        long long a, b, c, d;
        cin >> a >> b >> c >> d;
        if (calculate_hash(b, a) == calculate_hash(d, c))
        {
            cout << "Yes" << endl;
        }
        else
        {
            cout << "No" << endl;
        }
    }
}