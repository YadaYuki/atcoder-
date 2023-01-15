N,M = map(int,input().split())
x_set = list()
for i in range(M):
    kx = list(map(int,input().split()))
    k = kx[0]
    x_set.append(set(kx[1:]))

for i in range(1,N):
    for j in range(i+1,N+1):
        ok = False
        for x in x_set:
            if (i in x) and (j in x):
                ok = True
        
        if not ok:
            print("No")
            exit()
print("Yes")

