#include <bits/stdc++.h>
using namespace std;

// 素因数分解
using pll = pair<long long, long long>; // (素因数, 指数)
vector<pll> prime_factorize(long long n)
{
    vector<pll> res;
    for (long long p = 2; p * p <= n; ++p)
    {
        if (n % p != 0)
            continue;
        long long e = 0;
        while (n % p == 0)
        {
            n /= p, ++e;
        }
        res.emplace_back(p, e);
    }
    if (n != 1)
        res.emplace_back(n, 1);
    return res;
}

// n が p で何回割れるかを求める
long long how_many(long long n, long long p)
{
    long long res = 0;
    while (n % p == 0)
    {
        n /= p;
        ++res;
    }
    return res;
}

int main()
{
    // 入力
    long long K;
    cin >> K;

    // K を素因数分解する
    vector<pll> pf = prime_factorize(K);

    // 各素因数ごとに求めていく
    long long res = 0;
    for (auto [p, e] : pf)
    {
        long long f = 0; // n! を素因数分解したときの p の指数
        for (long long n = p; true; n += p)
        {
            f += how_many(n, p);
            if (f >= e)
            {
                res = max(res, n);
                break;
            }
        }
    }
    cout << res << endl;
}