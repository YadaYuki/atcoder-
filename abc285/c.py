S = list(input())
S.reverse()
ans = 0
for i,c in enumerate(S):
    ans += (26 ** i) * (ord(c) - ord("A") + 1) 
print(ans)
