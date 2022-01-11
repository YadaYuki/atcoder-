N = int(input())
S = input()

ans = 0
nj = 0

for j in range(1,N):
    if S[j] == S[j-1]:
        nj += 1
    else:
        nj = 0
    ans += nj

print(ans)

