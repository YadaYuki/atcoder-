#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<ll> C(9);
    ll min_C = 1e6 + 1;
    for (int i = 0; i < 9; i++)
    {
        cin >> C[i];
        min_C = min(min_C, C[i]);
    }
    ll max_digit = N / min_C;
    string ans = "";

    for (int i = 0; i < max_digit; i++)
    {
        for (int j = 8; j >= 0; j--)
        {
            ll rest_digit = max_digit - (i + 1);
            ll rest_N = N - C[j];
            auto can_fill_rest_digit = rest_digit <= (rest_N / min_C) && (rest_N >= 0);
            if (can_fill_rest_digit)
            {
                N -= C[j];
                ans.push_back((char)('0' + (j + 1)));
                break;
            }
        }
    }
    cout << ans << endl;
}