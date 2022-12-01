// https://onlinejudge.u-aizu.ac.jp/problems/2013
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

#define ll long long
using namespace std;

vector<string> split(const string &s, char delim)
{
    vector<string> elems;
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim))
    {
        if (!item.empty())
        {
            elems.push_back(item);
        }
    }
    return elems;
}

int main()
{
    int N;
    while (true)
    {
        cin >> N;
        if (N == 0)
        {
            break;
        }
        ll day_sec = 86400;
        vector<int> imos(day_sec, 0);
        for (int i = 0; i < N; i++)
        {
            string from, to;
            cin >> from >> to;
            vector<string> from_vec = split(from, ':');
            vector<string> to_vec = split(to, ':');
            int from_sec = stoi(from_vec[0]) * 60 * 60 + stoi(from_vec[1]) * 60 + stoi(from_vec[2]);
            int to_sec = stoi(to_vec[0]) * 60 * 60 + stoi(to_vec[1]) * 60 + stoi(to_vec[2]);
            imos[from_sec] += 1;
            imos[to_sec] -= 1;
        }
        for (int i = 1; i < day_sec; i++)
        {
            imos[i] = imos[i] + imos[i - 1];
        }
        int ans = -1;
        for (int i = 0; i < day_sec; i++)
        {
            ans = max(imos[i], ans);
        }
        cout << ans << endl;
    }
}
