#include <bits/stdc++.h>
using namespace std;
 
#define ll long long

int main() {
  ll N,X;
  cin >> N >> X;
  vector<char> S(N);
  for(ll i=0;i<N;i++) cin >> S[i];
  vector<char> stack;
  for (ll i=0;i<N;i++) {
    if(S[i]=='U'){
        if(stack.empty()){
            X /= 2;
        }else{
            stack.pop_back();
        }
    }else{
        stack.push_back(S[i]);
    }
  }
  for (ll i=0;i<stack.size();i++) {
    if(stack[i]=='L'){
        X *= 2;
    }else{
        X *= 2;
        X += 1;
    }
  }
    cout << X << endl;
}