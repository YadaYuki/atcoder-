#include <bits/stdc++.h>
using namespace std;

int main()
{
    int Q;
    cin >> Q;
    set<int> s;
    for (int i = 0; i < Q; i++)
    {
        int q,x;
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
            auto iter = s.lower_bound(x);
            if (iter == s.end())
                cout << -1 << endl;
            else
                cout << *iter << endl;
            break;
        }
    }
}