#include <bits/stdc++.h>
#define ll long long
using namespace std;

int coordinate_to_idx(int c)
{
    return c + 10000;
}

int main()
{
    int N, x, y;
    cin >> N >> x >> y;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    vector<int> A_odd(N / 2 + N % 2); // xを作る
    vector<int> A_even(N / 2);        // yを作る
    for (int i = 0; i < N; i++)
    {
        if (i % 2 == 0)
        {
            A_odd[i / 2] = A[i];
        }
        if (i % 2 == 1)
        {
            A_even[i / 2 - 1] = A[i];
        }
    }
    vector<vector<bool>> x_dp(A_odd.size() + 1, vector<bool>(20010));
    vector<vector<bool>> y_dp(A_even.size() + 1, vector<bool>(20010));

    cout << x_dp.size() << ","  << y_dp.size() << endl;

    x_dp[0][coordinate_to_idx(0)] = true;
    x_dp[1][coordinate_to_idx(A_odd[0])] = true;
    y_dp[0][coordinate_to_idx(0)] = true;

    for (unsigned long i = 0; i < A_odd.size(); i++)
    {
        for (int j = -10000; j < 100001; j++)
        {
            if (j - A_odd[i] >= -10000)
            {
                x_dp[i + 1][coordinate_to_idx(j)] = x_dp[i][coordinate_to_idx(j - A_odd[i])] || x_dp[i + 1][coordinate_to_idx(j)];
            }
            if (j + A_odd[i] <= 10000)
            {
                x_dp[i + 1][coordinate_to_idx(j)] = x_dp[i][coordinate_to_idx(j + A_odd[i])] || x_dp[i + 1][coordinate_to_idx(j)];
            }
        }
    }
    for (unsigned long i = 0; i < A_even.size(); i++)
    {
        for (int j = -10000; j < 100001; j++)
        {
            if (j - A_even[i] >= -10000)
            {
                y_dp[i + 1][coordinate_to_idx(j)] = y_dp[i][coordinate_to_idx(j - A_even[i])] || y_dp[i + 1][coordinate_to_idx(j)];
            }
            if (j + A_even[i] <= 10000)
            {
                y_dp[i + 1][coordinate_to_idx(j)] = y_dp[i][coordinate_to_idx(j + A_even[i])] || y_dp[i + 1][coordinate_to_idx(j)];
            }
        }
    }

    if (x_dp[x_dp.size() - 1][coordinate_to_idx(x)] && y_dp[y_dp.size() - 1][coordinate_to_idx(y)])
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
}