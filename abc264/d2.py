S = list(input())
target = list("atcoder")

ans = 0
for i,c in enumerate(target):
    s_idx = S.index(c)
    cost = s_idx - i
    ans += cost
    while s_idx != i:
        S[s_idx],S[s_idx-1] = S[s_idx-1],S[s_idx]
        s_idx -= 1
    

print(ans)