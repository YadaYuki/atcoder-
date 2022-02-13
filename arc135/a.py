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


# ans = 1
# MOD = 998244353
# for num in num_in_board:
#     ans *= num
#     ans %= MOD


# if X < 5:
#     print(X)
#     exit()

# # candidates = deque([X])
# num_in_board = []


# # 同じ問題
# while len(candidates) > 0:
#     num = candidates.popleft()
#     xu = num // 2
#     xd = num // 2 if num % 2 == 0 else num // 2 + 1
#     for x in [xu, xd]:
#         if x < 5:
#             num_in_board.append(x)
#         else:
#             candidates.append(x)