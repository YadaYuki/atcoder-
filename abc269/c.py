N = int(input())
active_bit_idxes = []
for i in range(60):
    if (N >> i & 1) == 1:
        active_bit_idxes.append(i)

K = len(active_bit_idxes) # <= 15
ans_ls = list()
for i in range(2**K):
    ans = 0
    for j in range(K):
        if (i >> j & 1) == 1:
            ans += 2 ** active_bit_idxes[j]
    ans_ls.append(ans)

for a in ans_ls:
    print(a)

