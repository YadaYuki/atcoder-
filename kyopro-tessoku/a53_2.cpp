#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    priority_queue<long long,vector<long long>,greater<long long> > pq;
    long long q;
    cin >> q;
    for(long long i = 0; i < q; i++)
    {
        long long x;
        cin >> x;
        if(x == 1)
        {
            long long y;
            cin >> y;
            pq.push(y);
        }
        else if(x == 2)
        {
            cout << pq.top() << endl;
        }
        else
        {
            pq.pop();
        }
    }
}
