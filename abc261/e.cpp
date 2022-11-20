#include <bits/stdc++.h>
using namespace std;
#define bit(x, i) (((x) >> (i)) & 1)

int main()
{
    int n, c;
    cin >> n >> c;
    vector<pair<int, int>> op(n);
    for (int i = 0; i < n; i++)
        cin >> op[i].first >> op[i].second;

    vector<int> ans(n);
    for (int k = 0; k < 30; k++)
    {

        array<int, 2> func = {0, 1};
        int crr = bit(c, k); // cのkビット目
        cout << crr << " ";
        for (int i = 0; i < n; i++)
        {
            auto t = op[i].first;
            auto a = op[i].second;
            array<int, 2> f;
            int x = bit(a, k);
            if (t == 1)
            {
                f = {0 & x, 1 & x};
            }
            if (t == 2)
            {
                f = {0 | x, 1 | x};
            }
            if (t == 3)
            {
                f = {0 ^ x, 1 ^ x};
            }
            func = {f[func[0]], f[func[1]]};
            crr = func[crr];
            ans[i] |= crr << k;
        }
    }

    for (int i = 0; i < n; i++)
        cout << ans[i] << endl;
}
