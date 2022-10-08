#include <bits/stdc++.h>
#define MAX_DATA 300000
#define MIN_VALUE -1000000000
using namespace std;

class SegmentTree
{
private:
    long long data[MAX_DATA]; // segTreeを構成する配列
    long long size;           // segTreeで管理する配列のサイズ

public:
    SegmentTree(long long seg_size)
    {
        // segTreeのサイズは、2のべき乗にする
        size = 1;
        while (size < seg_size)
            size *= 2;
        // segTreeの初期化
        for (int i = 1; i < 2 * size; i++)
            data[i] = 0;
    }

    long long get_size()
    {
        return size;
    }

    void update(long long k, long long v)
    {
        k += size - 1;
        data[k] = v;
        while (k > 1)
        {
            k /= 2;
            data[k] = data[2 * k] + data[2 * k + 1];
        }
    }

    long long query(long long l, long long r, long long cur_l, long long cur_r, long long cur)
    {
        bool is_in = (l <= cur_l && cur_r <= r);
        bool is_out = (r <= cur_l || cur_r <= l);
        if (is_in)
            return data[cur];
        if (is_out)
            return 0;
        long long mid = (cur_l + cur_r) / 2;
        long long left = query(l, r, cur_l, mid, 2 * cur);
        long long right = query(l, r, mid, cur_r, 2 * cur + 1);
        return left + right;
    }
};

int main()
{
    long long N, Q;
    cin >> N >> Q;
    auto s = SegmentTree(N);
    for (int i = 0; i < Q; i++)
    {
        int q;
        cin >> q;
        if (q == 1)
        {
            long long p, x;
            cin >> p >> x;
            s.update(p, x);
        }
        if (q == 2)
        {
            long long l, r;
            cin >> l >> r;
            cout << s.query(l, r, 1, s.get_size() + 1, 1) << endl;
        }
    }
}