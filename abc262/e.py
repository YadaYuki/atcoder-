from operator import mul
from functools import reduce

def comb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

MOD = 998244353
N,M,K = map(int,input().split())
graph = [[] for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)

verticals_with_odd_degree = 0
verticals_with_even_degree = 0

for n in range(N):
    if len(graph[n]) % 2 == 0:
        verticals_with_even_degree += 1
    else:
        verticals_with_odd_degree += 1

# verticals_with_odd_degreeから偶数個(red_verticals_with_odd_degree)選んで、
# 残りのK-red_verticals_with_odd_degree個をverticals_with_even_degreeから選ぶ

ans = 0
for red_verticals_with_odd_degree in range(0,verticals_with_odd_degree+1,2):
    
    if K < red_verticals_with_odd_degree:
        break
    red_verticals_with_even_degree = K - red_verticals_with_odd_degree
    ans = (ans + comb(verticals_with_odd_degree, red_verticals_with_odd_degree) * comb(verticals_with_even_degree, red_verticals_with_even_degree)) % MOD

ans %= MOD

print(ans)