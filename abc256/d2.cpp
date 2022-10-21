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
    vector<pair<int, int>> ans;

    int l_union = LR[0].first;
    int r_max = LR[0].second;
    for (auto lr : LR)
    {
        int l = lr.first;
        int r = lr.second;
        if (r_max < l)
        {
            ans.push_back(pair{l_union, r_max});
            l_union = l;
        }
        r_max = max(r, r_max);
    }
    ans.push_back(pair{l_union, r_max});
    for(auto lr:ans){
        cout << lr.first << " " << lr.second << endl;
    }
}