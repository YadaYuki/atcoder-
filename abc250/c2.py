N,Q = map(int,input().split())
x = []
for _ in range(Q):
    x.append(int(input()))

a = [i+1 for i in range(N)]
idx_dict = {a[i]:i for i in range(N)}
for xi in x:
    xi_idx = idx_dict[xi]
    exchange_idx = xi_idx+1 if xi_idx != N-1 else N-2
    idx_dict[xi] = exchange_idx
    idx_dict[a[exchange_idx]] = xi_idx
    a[xi_idx],a[exchange_idx] = a[exchange_idx],a[xi_idx]


print(*a)