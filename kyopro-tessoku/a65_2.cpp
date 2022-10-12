#include <bits/stdc++.h>
using namespace std;

vector<vector<int> > tree;
vector<int> subordinates;

int dfs(int p, int c)
{
    auto is_root = c == 0;
    auto is_leaf = (!is_root) && (tree[c].size() == 1);
    if (is_leaf)
    {
        subordinates[c] = 0;
        return 1;
    }
    int total_subordinate = 0;
    for (auto n : tree[c])
    {
        if (p != n)
        {
            total_subordinate += dfs(c, n);
        }
    }
    subordinates[c] = total_subordinate;
    return total_subordinate + 1;
}

int main()
{
    int N;
    cin >> N;
    tree.assign(N, vector<int>());
    subordinates.assign(N, 0);
    for (int subordinate = 1; subordinate < N; subordinate++)
    {
        int superior;
        cin >> superior;
        superior--;
        tree[superior].push_back(subordinate);
        tree[subordinate].push_back(superior);
    }
    dfs(-1, 0);
    for (auto subordinate : subordinates)
    {
        cout << subordinate << " ";
    }
}