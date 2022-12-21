#include <bits/stdc++.h>
#define ll long long
using namespace std;

class TreeNode
{
private:
    int parent;
    vector<int> children;
    ll value;

public:
    TreeNode(int p, ll v)
    {
        parent = p;
        value = v;
    }
    void add_children(int c)
    {
        children.push_back(c);
    }
    int get_parent()
    {
        return parent;
    }
    ll get_value()
    {
        return value;
    }
};

int main()
{
    int Q;
    cin >> Q;
    map<int, int> note;
    vector<TreeNode> tree;
    tree.push_back(TreeNode(0, -1));
    vector<ll> ans;
    int cur_tail_A = 0;
    for (int i = 0; i < Q; i++)
    {
        string s;
        cin >> s;
        if (s == "ADD")
        {
            ll x;
            cin >> x;
            tree.push_back(TreeNode(cur_tail_A, x));
            tree[cur_tail_A].add_children(tree.size() - 1);
            cur_tail_A = tree.size() - 1;
        }
        if (s == "DELETE")
        {
            cur_tail_A = tree[cur_tail_A].get_parent();
        }
        if (s == "SAVE")
        {
            int y;
            cin >> y;
            note[y] = cur_tail_A;
        }
        if (s == "LOAD")
        {
            int z;
            cin >> z;
            cur_tail_A = note[z];
        }
        ans.push_back(tree[cur_tail_A].get_value());
    }
    for (auto a : ans)
    {
        cout << a << " ";
    }
    cout << endl;
}