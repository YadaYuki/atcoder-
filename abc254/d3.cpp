#include <bits/stdc++.h>
#include <cmath>
#define ll long long
using namespace std;

bool is_squere(int N)
{
    int r = (int)floor(sqrt((long double)N)); // 切り捨てした平方根
    return (r * r) == N;
}

int main()
{
    int N;
    cin >> N;
    vector<vector<int>> divisors(N + 1);
    for (int i = 1; i <= N; i++)
    {
        for (int div = 1; div * div <= N; div++)
        {
            if (i % div == 0)
            {
                divisors[i].push_back(div);
                if (div * div != i)
                {
                    divisors[i].push_back(i / div);
                }
            }
        }
        sort(divisors[i].begin(), divisors[i].end());
    }
    map<int, int> ifi2cnt;
    for (int i = 1; i <= N; i++)
    {
        int fi = -1;
        for (auto divisor : divisors[i])
        {
            if (is_squere(divisor))
            {
                fi = divisor;
            }
        }
        int ifi = i / fi;
        ifi2cnt[ifi] += 1;
    }
    long long ans = 0;
    for (auto iter = ifi2cnt.begin(); iter != ifi2cnt.end(); iter++)
    {
        ans += iter->second * iter->second;
    }
    cout << ans << endl;
}