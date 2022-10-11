#include <bits/stdc++.h>
using namespace std;

vector<int> num_of_subordinates;
vector<vector<int> > tree;

// 一発で解けたの嬉しい〜〜〜！

int calculate_num_of_subordinates(int p, int c)
{
    auto is_root = (c == 0);
    auto is_leaf = (!is_root) && (tree[c].size() == 1);
    if (is_leaf)
    { // there are no subordinates.
        num_of_subordinates[c] = 0;
        return num_of_subordinates[c] + 1; // 部下の数 + 自分
    }

    int total_num_of_subordinates = 0;
    for (auto next : tree[c])
    {
        auto is_parent = (next == p);
        if (is_parent)
        {
            continue;
        }
        total_num_of_subordinates += calculate_num_of_subordinates(c, next);
    }

    num_of_subordinates[c] = total_num_of_subordinates;
    return total_num_of_subordinates + 1;
}

int main()
{
    int N;
    cin >> N;

    tree.assign(N, vector<int>());
    num_of_subordinates.assign(N, -1);
    for (int subordinate = 1; subordinate < N; subordinate++)
    {
        int boss;
        cin >> boss;
        boss--;
        tree[subordinate].push_back(boss);
        tree[boss].push_back(subordinate);
    }

    calculate_num_of_subordinates(-1,0);

    for(auto num_of_subordinate:num_of_subordinates){
        cout << num_of_subordinate << " ";
    }
}