#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, K;
    cin >> N >> K;
    vector<int> P(N);
    for (int i = 0; i < N; i++)
    {
        cin >> P[i];
    }

    vector<int> piles(N + 1);
    vector<int> under(N + 1, -1);
    vector<int> ans(N + 1, -1);
    set<int> s;

    for (int i = 0; i < N; i++)
    {
        auto x = P[i];
        auto x_lower_bound = s.lower_bound(x);
        if (x_lower_bound == s.end())
        {
            s.insert(x);
            piles[x] = 1;
        }
        else
        {
            auto v = *x_lower_bound;
            under[x] = v;
            piles[x] = piles[v] + 1;
            s.erase(v);
            s.insert(x);
        }

        if (piles[x] == K)
        {
            auto eaten = i + 1;
            s.erase(x);
            while (x != -1)
            {
                ans[x] = eaten;
                x = under[x];
            }
        }
    }
    for (int i = 1; i <= N; i++)
    {
        cout << ans[i] << endl;
    }
}