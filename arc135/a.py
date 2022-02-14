# from queue import deque
from collections import defaultdict

X = int(input())

MOD = 998244353
ans_d = defaultdict(int)
def dfs(n):
    if n < 5:
        return n
    else:
        if ans_d[n] != 0:
            return ans_d[n]
        else:
            ans_d[n] = dfs(n // 2) * dfs(n // 2 + (n % 2)) % MOD
            return ans_d[n]

print(dfs(X))
