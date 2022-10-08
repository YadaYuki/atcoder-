#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long Q;
    cin >> Q;
    priority_queue<long long, vector<long long>, greater<long long> > pq;
    for (long long i = 0; i < Q; i++)
    {
        long long q;
        long long price;
        cin >> q;
        switch (q)
        {
        case 1:
            cin >> price;
            pq.push(price);
            break;
        case 2:
            cout << pq.top() << endl;
            break;
        case 3:
            pq.pop();
            break;
        }
    }
}