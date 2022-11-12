from collections import defaultdict
N,K = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a)

val_to_origin_idx = defaultdict(list)

for i in range(N):
    val_to_origin_idx[a[i]].append(i)

print(val_to_origin_idx)

for sorted_idx in range(N):
    v = sorted_a[sorted_idx]
    ok = False
    for idx in range(len(val_to_origin_idx[v])):
        v_idx = val_to_origin_idx[v][idx]
        print(v,v_idx,sorted_idx)
        if v_idx == -1:
            continue
        else:
            if abs(v_idx - sorted_idx) % K == 0:
                ok = True
                val_to_origin_idx[v][idx] = -1
    if not ok:
        print("No")
        exit()

print("Yes")