#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    vector<int> L;

    for (int i = 0; i < N; i++)
    {

        unsigned long pos = lower_bound(L.begin(), L.end(), A[i]) - L.begin();
        if (pos == L.size())
        {
            L.push_back(A[i]);
        }
        else
        {
            L[pos] = A[i];
        }
    }
    cout << L.size() << endl;
}