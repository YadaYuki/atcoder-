#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, K;
    cin >> N >> K;
    vector<int> P;
    for (int i = 0; i < N; i++)
    {
        int p;
        cin >> p;
        P.push_back(p);
    }
    vector<int> ans;
    ans.assign(N + 1, -1);

    vector<int> under;
    under.assign(N + 1, -1); // カードiの下にあるカード

    vector<int> piles;
    piles.assign(N + 1, 0);

    set<int> numbers_in_stages;

    for (int i = 0; i < N; i++)
    {
        auto p = P[i];
        auto lower_bound_p_itr = numbers_in_stages.lower_bound(p);
        bool is_exist = lower_bound_p_itr != numbers_in_stages.end();
        if (!is_exist)
        {
            numbers_in_stages.insert(p);
            piles[p] += 1;
        }
        else
        {
            auto lower_bound_p = (*lower_bound_p_itr);
            // cout << lower_bound_p << ", " << p << endl;
            numbers_in_stages.insert(p);
            under[p] = lower_bound_p;
            piles[p] = piles[lower_bound_p] + 1;
            numbers_in_stages.erase(lower_bound_p);
        }
        if (piles[p] == K)
        {
            numbers_in_stages.erase(p);
            // cout << "p: " << p << ", piles[p]: " << piles[p] << endl;
            while (p != -1)
            {
                ans[p] = i + 1;
                p = under[p];
            }

        }
        // for (int j = 0; j < N + 1; j++)
        // {
        //     cout << under[j] << endl;
        // }
    }
    for (int i = 1; i < N + 1; i++)
    {
        cout << ans[i] << endl;
    }
}