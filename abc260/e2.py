N,M = map(int,input().split())
A,B = [],[]
ans = [0] * (M + 2)
pair = [-1] * (M + 1)

for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    pair[a] = max(pair[a],b)

r = max(A)
for l in range(1,min(B) + 1):
    ans[r-l+1] += 1
    ans[M-l+2] -= 1
    if pair[l] > 0:
        r = max(pair[l],r)

for i in range(1,M+1):
    ans[i] += ans[i-1]

print(*ans[1:M+1])

