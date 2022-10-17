#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    set<int> s;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int q, x;
        cin >> q >> x;
        if (q == 1)
        {
            s.insert(x);
        }
        if (q == 2)
        {
            s.erase(x);
        }
        if (q == 3)
        {
            auto lb = s.lower_bound(x);

            if (lb == s.end())
            {
                cout << -1 << endl;
            }
            else
            {
                // cout << "HERE" << endl;
                cout << *lb << endl;
            }
        }
    }
}