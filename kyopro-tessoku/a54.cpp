#include <bits/stdc++.h>
using namespace std;

int main()
{
    map<string, long long> students_to_scores_map;
    long long q;
    cin >> q;
    for (long long i = 0; i < q; i++)
    {
        string name;
        long long query;
        cin >> query >> name;
        if (query == 1)
        {
            long long score;
            cin >> score;
            students_to_scores_map[name] = score;
        }
        else if (query == 2)
        {
            cout << students_to_scores_map[name] << endl;
        }
    }
}