N,L = map(int,input().split())
ans = []
for i in range(N):
    v = i
    a = []
    for j in range(L-1):
        a.append(v%3)
        v = v // 3
    a.reverse()
    
    for d in [0,1,2]:
        base_prefix = chr(ord("2") - d)
        s = base_prefix
        for j in range(L-1):
            s += str((a[j]+d)%3)
        ans.append(s)

for i in ans:
    print(i)