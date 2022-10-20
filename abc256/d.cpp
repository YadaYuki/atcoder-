#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<pair<int, int>> LR;
    for (int i = 0; i < N; i++)
    {
        int l, r;
        cin >> l >> r;
        LR.push_back(pair{l, r});
    }
    sort(LR.begin(), LR.end());
    int cur_l = LR[0].first;
    int cur_max_r = LR[0].second;
    vector<pair<int, int>> ans;
    for (auto lr : LR)
    {
        int l = lr.first;
        int r = lr.second;
        if (cur_max_r < l)
        {
            ans.push_back({cur_l, cur_max_r});
            cur_l = l;
        }
        cur_max_r = max(r, cur_max_r);
    }
    ans.push_back({cur_l, cur_max_r});
    for (auto lr : ans)
    {
        cout << lr.first << " " << lr.second << endl;
    }
}