#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll N, M;
    cin >> N >> M;
    vector<ll> A(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    vector<set<ll>> op_set(M + 1);
    for (ll i = 0; i < N; i++)
    {
        auto idx = i + 1;
        auto a = A[i];
        ll first_important_num = -1;
        ll op_cnt_2_first_important_num = -1;
        if (a < 0)
        {
            op_cnt_2_first_important_num = (0 - a) / idx + 1;
            if ((0 - a) % idx == 0)
            {
                op_cnt_2_first_important_num -= 1;
            }
            first_important_num = a + op_cnt_2_first_important_num * idx;
        }
        else if (a > N)
        {
            continue; // aがimportant_numになることはない
        }
        else
        {
            first_important_num = a;
            op_cnt_2_first_important_num = 0;
        }
        ll important_num = first_important_num;
        ll op_cnt = op_cnt_2_first_important_num;
        while ((op_cnt <= M) && (important_num <= N))
        {
            op_set[op_cnt].insert(important_num);
            op_cnt += 1;
            important_num += idx;
        }
    }
    for (int i = 1; i <= M; i++)
    {
        ll ans = 0;
        while (op_set[i].find(ans) != op_set[i].end())
        {
            ans += 1;
        }
        cout << ans << endl;
    }
}