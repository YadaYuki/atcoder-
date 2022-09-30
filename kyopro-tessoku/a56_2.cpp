#include <bits/stdc++.h>
using namespace std;

long long MAX_Q = 200000;
long long MAX_N = 200000;

int main()
{
    long long N, Q;
    cin >> N >> Q;
    string S;
    cin >> S;
    long long L = 100;
    vector<long long> Hash(MAX_N + 1); // Hash[i] = Hash of S[0..i-1]
    long long MOD = 1000000007;
    // Hashの計算
    Hash[0] = 0;
    for (long long i = 1; i <= N; i++)
    {
        Hash[i] = (Hash[i - 1] * 100LL + (S[i - 1] - 'a' + 1)) % MOD;
    }
    // 累乗を事前に計算しておく
    vector<long long> POWER_L(MAX_N + 1);
    POWER_L[0] = 1;
    for (long long i = 1; i <= N; i++)
    {
        POWER_L[i] = (POWER_L[i - 1] * L) % MOD; // MODが必要である点に注意
    }

    for (long long i = 0; i < Q; i++)
    {
        long long a, b, c, d;
        cin >> a >> b >> c >> d;
        //  S[a..b] == S[c..d] かどうかを判定
        long long length = b - a + 1;
        long long hash_A_B = Hash[b] - (Hash[a - 1] * POWER_L[length]) % MOD;
        if (hash_A_B < 0)
            hash_A_B += MOD;
        long long hash_C_D = Hash[d] - (Hash[c - 1] * POWER_L[length]) % MOD;
        if (hash_C_D < 0)
            hash_C_D += MOD;
        if (hash_A_B == hash_C_D)
        {
            cout << "Yes" << endl;
        }
        else
        {
            cout << "No" << endl;
        }
    }
}