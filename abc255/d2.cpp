#include <bits/stdc++.h>
#define ll long long
using namespace std;

class SegmentTree
{
private:
    vector<ll> data;
    ll size;

    ll dfs(ll l, ll r, ll cl, ll cr, ll cur_idx)
    {
        auto is_in = (l <= cl) && (cr <= r);
        auto is_out = (cr <= l) || (r <= cl);
        if (is_in)
        {
            return data[cur_idx];
        }
        if (is_out)
        {
            return 0;
        }
        auto mid = (cl + cr) / 2;
        auto left_sum = dfs(l, r, cl, mid, cur_idx * 2);
        auto right_sum = dfs(l, r, mid, cr, cur_idx * 2 + 1);
        return left_sum + right_sum;
    }

public:
    explicit SegmentTree(ll n)
    {
        size = 1;
        while (n > size)
        {
            size *= 2;
        }
        data.assign(size * 2, 0);
    }

    void print_data()
    {
        for (int i = size; i < size * 2; i++)
        {
            cout << data[i] << " ";
        }
        cout << endl;
    }

    void update(ll pos, ll x)
    {
        data[pos + size - 1] = x;
        ll node_idx = pos + size - 1;
        while (node_idx > 0)
        {
            node_idx /= 2;
            data[node_idx] = data[node_idx * 2] + data[node_idx * 2 + 1];
        }
    }

    ll rsq(ll l, ll r)
    {
        return dfs(l, r, 1, size + 1, 1);
    }
};

int main()
{
    ll N, Q;
    cin >> N >> Q;
    vector<ll> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    sort(A.begin(), A.end());
    auto st = SegmentTree(N);
    for (int i = 0; i < N; i++)
    {
        st.update(i + 1, A[i]);
    }
    for (int i = 0; i < Q; i++)
    {
        ll x;
        cin >> x;
        auto ptr = upper_bound(A.begin(), A.end(), x);
        ll v_cnt_bigger_than_x = A.end() - ptr;
        ll v_cnt_less_than_or_equal_x = ptr - A.begin();
        ll less_sum = st.rsq(1, 1 + v_cnt_less_than_or_equal_x);
        ll bigger_sum = st.rsq(1 + v_cnt_less_than_or_equal_x, N + 1);
        ll ans = (x * v_cnt_less_than_or_equal_x - less_sum) + (bigger_sum - x * v_cnt_bigger_than_x);
        cout << ans << endl;
    }
}