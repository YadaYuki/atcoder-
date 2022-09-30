#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long Q;
    cin >> Q;
    map<string, long long> m;
    for(long long i=0;i<Q;i++){
        long long q;
        string x;
        cin >> q;
        if(q == 1){
            long long y;
            cin >> x >> y;
            m[x] += y;
        }else{
            cin >> x;
            cout << m[x] << endl;
        }

    }
}