N = int(input())
p = list(map(int,input().split()))
p_to_idx = [-1 for i in range(N)]
for i,pp in enumerate(p):
    p_to_idx[pp] = i

i_to_nor = [None for i in range(N)]

for i in range(N):
    nor = (i-p_to_idx[i]) % N
    i_to_nor[i] = [
        (nor-1)%N,nor,(nor+1)%N
    ]

nor_to_cnt = [0 for i in range(N)]
for i in range(N):
    nor_cnd = i_to_nor[i]
    for n in nor_cnd:
        nor_to_cnt[n] += 1

ans = max(nor_to_cnt)
print(ans)