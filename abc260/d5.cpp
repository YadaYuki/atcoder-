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
    vector<int> under(N + 1, -1), piles(N + 1, 0), ans(N + 1, -1);
    set<int> s;
    for (int i = 0; i < N; i++)
    {
        auto p = P[i];
        auto p_lower_bound = s.lower_bound(p);
        if (p_lower_bound == s.end())
        {
            s.insert(p);
            piles[p] = 1;
        }
        else
        {
            s.insert(p);
            s.erase(*p_lower_bound);
            under[p] = *p_lower_bound;
            piles[p] = piles[*p_lower_bound] + 1;
        }

        if (piles[p] == K)
        {
            s.erase(p);
            while (p != -1)
            {
                ans[p] = i + 1;
                p = under[p];
            }
        }
    }

    for (int i = 1; i <= N; i++)
    {
        cout << ans[i] << endl;
    }
}