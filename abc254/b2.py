N = int(input())
a = []
for i in range(N):
    a.append([1 for i in range(i+1)])

for i in range(N):
    for j in range(i+1):
        if not (j == 0 or j == i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
        

for i in range(N):
    print(*a[i])