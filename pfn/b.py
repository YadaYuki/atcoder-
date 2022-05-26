
def binary_str(n:int,d:int) -> str:
    return bin(n)[2:].zfill(d)


def get_pattern_idx(bin_str):
    pattern_idxes = []
    for i,bit in enumerate(bin_str):
        if bit == "1":
            pattern_idxes.append(i)
    return pattern_idxes

# 最短処理数を求める課題であるため、BFSにより実装を行った
def solve(N,W,items) -> int: #items: [(w,v,r),...]
    X_sum_pattern = []
    for x_pattern in range(1 << N):
        x_pattern_idxes = get_pattern_idx(binary_str(x_pattern, N))
        X = [items[i] for i in x_pattern_idxes]
        X_w_s = sum([x[0] for x in X])
        if X_w_s > W:
            continue
        X_v_s = sum([x[1] for x in X])
        X_r_s = sum([x[2] for x in X])
        X_sum_pattern.append((X_w_s, X_v_s, X_r_s))

    X_sum_pattern.sort(key=lambda x: (x[1],x[2]), reverse=True)
    
    ans = 1 
    max_r = X_sum_pattern[0][2]
    for i in range(1,len(X_sum_pattern)):
        _, x_v_i, x_r_i = X_sum_pattern[i]
        if x_r_i >= max_r:
            ans += 1
        max_r = max(max_r, x_r_i)

    return ans

N,W = map(int,input().split()) # N=20
items = []
for _ in range(N):
    w,v,r = map(int,input().split())
    items.append([w,v,r])

print(solve(N,W,items))