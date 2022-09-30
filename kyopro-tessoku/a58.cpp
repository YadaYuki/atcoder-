#include <bits/stdc++.h>
using namespace std;

class SegmentTree
{
private:
    int n;
    vector<int> data;

public:
    int get_n() { return n; }
    void init(int N)
    {
        n = 1;
        while (n < N)
            n *= 2;
        int node_size_of_tree = 2 * n - 1;
        data = vector<int>(node_size_of_tree, 0);
    }
    void update(int pos, int x)
    {
        pos = pos + n - 1; // 葉のノード
        data[pos] = x;
        while (pos > 1)
        {
            pos /= 2;
            data[pos] = max(data[2 * pos], data[2 * pos + 1]);
        }
    }

    int query(int l, int r, int a, int b, int u)
    {
        if (r <= a || b <= l)
            return -1000000000;
        if (l <= a && b <= r)
            return data[u];
        int m = (a + b) / 2;
        int vl = query(l, r, a, m, 2 * u);
        int vr = query(l, r, m, b, 2 * u + 1);
        return max(vl, vr);
    }
};

int main()
{
    int N, Q;
    cin >> N >> Q;
    SegmentTree st;
    st.init(N);
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
        else
        {
            int l, r;
            cin >> l >> r;
            cout << st.query(l, r, 1, st.get_n()+1, 1) << endl;
        }
    }
}