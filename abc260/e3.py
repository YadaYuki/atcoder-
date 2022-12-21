N,M = map(int,input().split())
A,B = [],[]
pair = [-1 for i in range(M+1)]
for i in range(N):
    a,b = list(map(int,input().split()))
    A.append(a)
    B.append(b)
    pair[a] = max(pair[a],b)


f = [0 for i in range(M+2)]


r = max(A)
B_min = min(B)
for l in range(1,B_min+1):
    f[r-l+1] += 1
    f[M-l+2] -= 1
    # k = r-l ~ M-l まで.
    # M-l以降は入らない.
    # rをpairの最大値で更新していくのは何故か？
    # : lのペアを入れないとSの条件を満たさないから.
    if pair[l] > 0:
        r = max(r,pair[l])

for i in range(M):
    f[i+1] += f[i]


print(*f[1:M+1])