#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long Q;
    set<long long> s;
    cin >> Q;
    for (long long i = 0; i < Q; i++)
    {
        long long q, x;
        cin >> q >> x;
        switch (q)
        {
        case 1:
            s.insert(x);
            break;
        case 2:
            s.erase(x);
            break;
        case 3:
            auto ptr_lb = s.lower_bound(x);
            if (ptr_lb == s.end())
            {
                cout << -1 << endl;
            }
            else
            {
                cout << *ptr_lb << endl;
            }

            break;
        }
    }
}