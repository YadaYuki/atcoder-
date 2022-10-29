MOD = 998244353
A,B,C,D,E,F = map(int,input().split())
ABC = (A * B)%MOD
ABC = (ABC * C) %MOD

DEF = (D*E)%MOD
DEF = (DEF * F) %MOD
# print(ABC,DEF)
ans = (ABC - DEF) % MOD
if ans < 0:
    ans += MOD

print(ans)