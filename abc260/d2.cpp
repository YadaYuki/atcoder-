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

    // under[i]: カードiの下にあるカード
    // pile[i]: カードiの下にあるカードの枚数 + 1
    vector<int> under(N + 1);
    under.assign(N + 1, -1);
    vector<int> pile(N + 1, 0);
    set<int> s;
    vector<int> ans(N + 1, -1);
    for (int i = 0; i < N; i++)
    {
        auto x = P[i];
        auto iter = s.lower_bound(x);
        if (iter == s.end())
        {
            s.insert(x);
            pile[x] = 1;
        }
        else
        {
            auto lb_x = *iter;
            s.insert(x);
            pile[x] = pile[lb_x] + 1;
            under[x] = lb_x;
            s.erase(lb_x);
        }

        if (pile[x] == K)
        {
            s.erase(x);
            while (x != -1)
            {
                ans[x] = i + 1;
                x = under[x];
            }
            
        }
    }
    for (int i = 1; i <= N; i++)
    {
        cout << ans[i] << endl;
    }
}