#include <bits/stdc++.h>
using namespace std;
#define MIN_VAL -10000000

class SegmentTree
{
private:
    int _size;
    vector<int> _data;

    int dfs(int left, int right, int cur_left, int cur_right, int node_idx)
    {
        auto is_in = (left <= cur_left) && (cur_right <= right);
        auto is_out = (cur_right <= left) || (right <= cur_left);
        if (is_in)
            return _data[node_idx];
        if (is_out)
            return MIN_VAL;
        int mid = (cur_left + cur_right) / 2;
        int left_max = dfs(left, right, cur_left, mid, node_idx * 2);
        int right_max = dfs(left, right, mid, cur_right, node_idx * 2 + 1);
        return max(left_max, right_max);
    }

public:
    explicit SegmentTree(int size)
    {
        // N以上の2の累乗の中での最小値を配列のサイズとする. 完全2分木の方がセグメント木で計算する上で都合が良いため。
        _size = 1;
        while (_size < size)
        {
            _size *= 2;
        }
        int node_cnt_in_tree = _size * 2 + 1; // _data[0]に関しては無視する。その方が子要素の指定等がやりやすいため
        _data.assign(node_cnt_in_tree, 0);
    }

    void update(int pos, int x)
    {
        auto node_idx = pos + _size - 1;
        _data[node_idx] = x;
        while (node_idx > 0)
        {
            node_idx /= 2;
            auto left = _data[node_idx * 2];
            auto right = _data[node_idx * 2 + 1];
            _data[node_idx] = max(left, right);
        }
    }

    int rmq(int left, int right)
    {
        return dfs(left, right, 1, _size + 1, 1);
    }
};

int main()
{
    int N, Q;
    cin >> N >> Q;
    auto st = SegmentTree(N);
    for (int i = 0; i < Q; i++)
    {
        int q;
        cin >> q;
        if (q == 1)
        {
            int pos, x;
            cin >> pos >> x;
            st.update(pos, x);
        }
        if (q == 2)
        {
            int l, r;
            cin >> l >> r;
            cout << st.rmq(l, r) << endl;
        }
    }
}