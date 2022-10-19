#include <bits/stdc++.h>
using namespace std;
#define ll long long

class SegmentTree
{
private:
    vector<ll> data;
    ll size;

    ll dfs(ll l, ll r, ll cl, ll cr, ll idx)
    {
        auto is_in = (l <= cl) && (cr < r);
        auto is_out = (cr < l) || (r <= cl);
        if (is_in)
        {
            return data[idx];
        }
        if (is_out)
        {
            return 0;
        }
        ll mid = (cl + cr) / 2;
        ll left = dfs(l, r, cl, mid, idx * 2);
        ll right = dfs(l, r, mid + 1, cr, idx * 2 + 1);
        return left + right;
    }

public:
    explicit SegmentTree(ll N)
    {

        size = 1;
        while (size < N)
        {
            size *= 2;
        }
        data.assign(size * 2, 0);
    }

    void update(ll pos, ll x)
    {
        ll idx = pos + size - 1;
        data[idx] = x;
        while (idx > 0)
        {
            idx = idx / 2;
            auto l = data[idx * 2];
            auto r = data[idx * 2 + 1];
            data[idx] = l + r;
        }
    }

    ll rsq(ll l, ll r)
    {
        return dfs(l, r, 1, size, 1);
    }
};

int main()
{
    ll N, Q;
    cin >> N >> Q;
    vector<ll> A(N);
    auto st = SegmentTree(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    for (ll i = 1; i <= N; i++)
    {
        st.update(i, A[i - 1]);
    }

    for (ll i = 0; i < Q; i++)
    {
        ll x;
        cin >> x;
        auto iter = upper_bound(A.begin(), A.end(), x);
        ll elem_cnt_bigger_than_x = A.end() - iter;
        ll elem_cnt_lower_x = N - elem_cnt_bigger_than_x;
        // cout << elem_cnt_bigger_than_x << ", " << elem_cnt_lower_x << endl;
        ll total_cost = 0;
        // cout << st.rsq(1, 1 + elem_cnt_lower_x) << ", " << st.rsq(elem_cnt_lower_x + 1, N + 1) << endl;
        total_cost += x * elem_cnt_lower_x - st.rsq(1, 1 + elem_cnt_lower_x);
        total_cost += st.rsq(elem_cnt_lower_x + 1, N + 1) - x * elem_cnt_bigger_than_x;
        cout << total_cost << endl;
    }
}