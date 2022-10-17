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
        data.assign(size * 2, 0);
    }

    void update(int pos, int x)
    {
        int idx = pos + size - 1;
        data[idx] = x;
        while (idx > 0)
        {
            idx = idx / 2;
            auto l = data[idx * 2];
            auto r = data[idx * 2 + 1];
            data[idx] = l + r;
        }
    }

    int rsq(int l, int r)
    {
        return dfs(l, r, 1, size, 1);
    }

    int dfs(int l, int r, int cl, int cr, int idx)
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
        int mid = (cl + cr) / 2;
        int left = dfs(l, r, cl, mid, idx * 2);
        int right = dfs(l, r, mid+1, cr, idx * 2 + 1);
        return left + right;
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
            cout << seg.rsq(l, r) << endl;
        }
        // seg.print_data();
    }
}