N,X = map(int,input().split())
a = []
L = []
pattern_count = 1
for _ in range(N):
    gift = list(map(int,input().split()))
    Li = gift[0]
    pattern_count *= Li
    L.append(Li)
    a.append(gift[1:])

def idx_to_arr(idx):
    ans = [0] * N
    weight_each_digit = [1] * N
    for i in range(N-1):
        weight_each_digit[i+1] = L[i] * weight_each_digit[i]
    for i in range(N-1,-1,-1):
        ans[i] = idx // weight_each_digit[i]
        idx = idx % weight_each_digit[i]
    return ans

ans = 0

for i in range(pattern_count):
    gift_idx_arr = idx_to_arr(i)

    ball = 1
    for i,gift_idx_arr in enumerate(gift_idx_arr):
        ball *= a[i][gift_idx_arr]
    if ball == X:
        ans += 1

print(ans)


