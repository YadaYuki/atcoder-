#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long N, Q;
    cin >> N >> Q;
    string S;
    cin >> S;
    int L = 27;
    long long MOD = 1e9 + 7;
    long long Hash[N + 1]; // Hash[i] = Hash of S[0..i-1]
    Hash[0] = 0;
    for (int i = 1; i <= N; i++)
    {
        Hash[i] = (Hash[i - 1] * L + S[i - 1]) % MOD;
    }

    long long Pow[N + 1]; // Pow[i] = L^i
    Pow[0] = 1;
    for (int i = 1; i <= N; i++)
    {
        Pow[i] = (Pow[i - 1] * L) % MOD;
    }

    for (int i = 0; i < Q; i++)
    {
        int a,b,c,d;
        cin >> a >> b >> c >> d;
        long long length = b - a + 1; // = d - c + 1
        long long hash_a2b = Hash[b] - (Hash[a - 1] * Pow[length]) % MOD;
        if(hash_a2b < 0) hash_a2b += MOD;
        long long hash_c2d = Hash[d] - (Hash[c - 1] * Pow[length]) % MOD;
        if(hash_c2d < 0) hash_c2d += MOD;
        if(hash_a2b == hash_c2d) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
}