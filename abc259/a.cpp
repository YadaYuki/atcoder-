#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M, X, T, D;
    cin >> N >> M >> X >> T >> D;
    int base = T - X * D;
    // int ans = base + X * M;
    int year = min(X,M);
    int ans = base + D * year;
    cout << ans << endl;
}