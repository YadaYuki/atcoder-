#include <bits/stdc++.h>
#define ll long long
using namespace std;

class SegmentTree
{
private:
    vector<ll> _tree_data;
    ll _size;

    ll dfs(ll l, ll r, ll cur_l, ll cur_r, ll idx_in_tree_data)
    {
        auto is_in = (l <= cur_l) && (cur_r <= r);
        auto is_out = (cur_r <= l) || (r <= cur_l);
        // cout << l << " " << r << " " << cur_l << " " << cur_r << " " << (is_in ? "in" : "no") << " " << (is_out ? "out" : "no") << endl;
        if (is_in)
        {
            return _tree_data[idx_in_tree_data];
        }
        if (is_out)
        {
            return 0;
        }
        auto mid = (cur_l + cur_r) / 2;
        auto left_sum = dfs(l, r, cur_l, mid, idx_in_tree_data * 2);
        auto right_sum = dfs(l, r, mid, cur_r, idx_in_tree_data * 2 + 1);
        return left_sum + right_sum;
    }

public:
    explicit SegmentTree(ll N)
    {
        _size = 1;
        while (_size < N)
        {
            _size *= 2;
        }
        _tree_data.assign(_size*2, 0); // _tree_data[0] is ignored.
    }

    void update(ll pos, ll x)
    {
        ll idx_in_tree_data = pos + _size - 1;
        _tree_data[idx_in_tree_data] = x;
        while (idx_in_tree_data > 0)
        {
            idx_in_tree_data /= 2;
            auto l = _tree_data[idx_in_tree_data * 2];
            auto r = _tree_data[idx_in_tree_data * 2 + 1];
            _tree_data[idx_in_tree_data] = l + r;
        }
    }

    void print_data()
    {
        for (int i = _size; i < _size * 2; i++)
        {
            cout << _tree_data[i] << " ";
        }
        cout << endl;
    }

    // 区間[l,r)内の和を計算する.
    ll rsq(ll l, ll r)
    {
        return dfs(l, r, 1, _size + 1, 1);
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
    for (int i = 1; i <= N; i++)
    {
        st.update(i, A[i - 1]);
    }
    // st.print_data();
    for (int i = 0; i < Q; i++)
    {
        ll x;
        cin >> x;
        // xより大きい要素.
        auto iter = upper_bound(A.begin(), A.end(), x);
        ll cnt_bigger_than_x = A.end() - iter;
        ll cnt_less_than_x_or_x = N - cnt_bigger_than_x;
        // cout << cnt_bigger_than_x << ", " << cnt_less_than_x_or_x << endl;
        ll sum_less_than_x_or_x = st.rsq(1, cnt_less_than_x_or_x + 1);
        ll sum_bigger_than_x = st.rsq(cnt_less_than_x_or_x + 1, N + 1);
        // cout << sum_less_than_x_or_x << ", " << sum_less_than_x_or_x << endl;
        ll ans = (sum_bigger_than_x - x * cnt_bigger_than_x) + (x * cnt_less_than_x_or_x - sum_less_than_x_or_x);
        cout << ans << endl;
    }
}
