#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<int> A(N), B(N);
    vector<int> pair_of_A(M + 1, -1);
    int max_A = -1;
    int min_B = 1e9;
    for (int i = 0; i < N; i++)
    {
        cin >> A[i] >> B[i];
        pair_of_A[A[i]] = max(B[i], pair_of_A[A[i]]);
        max_A = max(max_A, A[i]);
        min_B = min(min_B, B[i]);
    }
    vector<int> f(M + 2, 0);

    int r = max_A;
    // lはB_minまで
    for (int l = 1; l < min_B + 1; l++)
    {
        // 配列を右から、というイメージを持たないほうが良い気がしている
        f[r - l + 1] += 1;
        f[M - l + 2] -= 1;
        if (pair_of_A[l] > 0)
        {
            r = max(r, pair_of_A[l]);
        }
    }

    for (int i = 1; i < M + 1; i++)
    {
        f[i] += f[i - 1];
    }

    for (int i = 1; i < M + 1; i++)
    {
        cout << f[i] << " ";
    }
    cout << endl;

}