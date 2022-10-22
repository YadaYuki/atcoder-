#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<pair<int, int>> LR(N);
    for (int i = 0; i < N; i++)
    {
        int l, r;
        cin >> l >> r;
        LR[i] = pair{l, r};
    }
    sort(LR.begin(), LR.end());
    int r_max = LR[0].second;
    int cur_l = LR[0].first;
    vector<pair<int, int>> ans;
    for (auto lr : LR)
    {
        auto l = lr.first;
        auto r = lr.second;
        if (l > r_max)
        {
            ans.push_back(pair{cur_l, r_max});
            cur_l = l;
        }
        r_max = max(r, r_max);
    }
    ans.push_back(pair{cur_l, r_max});
    for (auto xy : ans)
    {
        cout << xy.first << " " << xy.second << endl;
    }
}