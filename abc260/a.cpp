#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
  string S;
  cin >> S;
  map<char, int> mp;
  for (int i = 0; i < 3; i++)
  {
    auto c = S.at(i);
    mp[c] += 1;
  }
  for(auto [k,v]:mp){
    if(v==1){
      cout << k << endl;
      exit(0);
    }
  }
  cout << -1 << endl;
}