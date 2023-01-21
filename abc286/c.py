N,A,B = map(int,input().split())
S = input()
ans = 10**18
for a in range(N):
    b = 0
    new_s = list()
    for idx in range(a,a+N):
        i = idx % N
        new_s.append(S[i])
    for i in range(N//2):
        pair = N - i - 1
        if new_s[i] != new_s[pair]:
            b += B
    ans = min(a*A+b,ans)

print(ans)
