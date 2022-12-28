S = list(input())
ans = 0
for c_target_idx,c_target in enumerate(list("atcoder")):
    c_origin_idx = S.index(c_target)
    ans += c_origin_idx - c_target_idx
    while c_origin_idx > 0:
        S[c_origin_idx],S[c_origin_idx-1] = S[c_origin_idx-1],S[c_origin_idx]
        c_origin_idx -= 1
        if c_origin_idx == c_target_idx:
            break

print(ans)

