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
        return query(l, r, 1, size, 1);
    }
    int query(int l, int r, int cl, int cr, int cur)
    {
        auto is_in = (l <= cl) && (cr < r);
        auto is_out = (cr < l) || (r <= cl);
        // cout << endl;
        // cout << l << " " << r << " " << cl << " " << cr << endl;
        if (is_in)
        {
            return data[cur];
        }
        if (is_out)
        {
            return -1000000000;
        }
        int mid = (cl + cr) / 2;
        // cout << (mid + 1) << " " << mid << endl;
        int max_l = query(l, r, cl, mid, cur*2);
        int max_r = query(l, r, mid + 1, cr, cur*2+1);
        int ans = max(max_l, max_r);
        return ans;
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