#include <bits/stdc++.h>
using namespace std;

class SegmentTree
{
private:
    vector<int> data;
    int size;

public:
    explicit SegmentTree(int N)
    {
        size = 1;
        while (size < N)
        {
            size *= 2;
        }
        data.assign(size * 2 + 1, 0);
    }

    void update(int pos, int x)
    {
        int idx = pos + size - 1;
        data[idx] = x;
        while (idx > 0)
        {
            idx /= 2;
            data[idx] = max(data[idx * 2], data[idx * 2 + 1]);
        }
    }

    void print_data()
    {
        for (auto x : data)
        {
            cout << x << " ";
        }
        cout << endl;
    }
    int rmq(int l, int r)
    {
        return query(l, r, 1, size+1, 1);
    }
    int query(int l, int r, int cur_l, int cur_r, int cur)
    {
        bool is_in = (l <= cur_l && cur_r <= r);
        bool is_out = (r <= cur_l || cur_r <= l);
        if (is_in)
            return data[cur];
        if (is_out)
            return -10000000;
        int mid = (cur_l + cur_r) / 2;
        int left = query(l, r, cur_l, mid, 2 * cur);
        int right = query(l, r, mid, cur_r, 2 * cur + 1);
        return max(left, right);
    }
};

int main()
{
    int N, Q;
    cin >> N >> Q;
    auto seg = SegmentTree(N);
    for (int i = 0; i < Q; i++)
    {
        int q;
        cin >> q;
        if (q == 1)
        {
            int pos, x;
            cin >> pos >> x;
            seg.update(pos, x);
        }
        if (q == 2)
        {
            int l, r;
            cin >> l >> r;
            cout << seg.rmq(l, r) << endl;
        }
        // seg.print_data();
    }
}