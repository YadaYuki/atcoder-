#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<ll> C(9);
    for (int i = 0; i < 9; i++)
    {
        cin >> C[i];
    }

    auto min_itr = min_element(C.begin(), C.end());
    ll min_C = *min_itr;
    ll digit = N / min_C;
    vector<int> ans;
    for (int d = digit - 1; d >= 0; d--)
    {
        for (int i = 8; i >= 0; i--)
        {
            auto ci = C[i];
            auto left_N = N - ci;
            if (left_N >= d * min_C)
            {
                ans.push_back(i+1);
                N = left_N;
                break;
            }
        }
    }
    for (auto a : ans)
    {
        cout << a;
    }
    cout << endl;
}