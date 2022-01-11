from  collections import defaultdict

N = int(input())
S = list(input())

s_removed = None

S_dict = defaultdict(int)

for i in range(N):
    s_removed = S[:i] + S[i+1:]
    S_dict[''.join(s_removed)] += 1
ans = 0
for value in S_dict.values():
    ans += value * (value - 1) // 2

print(ans)


