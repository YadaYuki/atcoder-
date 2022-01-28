n = int(input())
p = list(map(int, input().split()))

def next_idx(idx):
    return (idx+1) % n

min_idx = p.index(1)
max_idx = p.index(n)

is_ascending = p[next_idx(min_idx)] == 2 # 初期配列が昇順かどうか

ans = -1
if is_ascending:
    if min_idx > n//2 + 1: # 反転 → 移動 → 反転
        ans = 2 + n - min_idx
    else:
        ans = min_idx
else:
    if max_idx > n//2: # 反転→移動
        ans = (n-max_idx) + 1 
    else: # 移動 → 反転
        ans = max_idx + 1

print(ans)
