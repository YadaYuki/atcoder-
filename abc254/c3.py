N,K = map(int,input().split())
a = list(map(int,input().split()))
a_mat_k = [[] for i in range(K)]

for i in range(K):
    for j in range(i,N,K):
        a_mat_k[i].append(a[j])

for i in range(K):
    a_mat_k[i].sort()
ans = []
for j in range(len(a_mat_k[0])):
    
    for i in range(K):
        if len(a_mat_k[i]) < j + 1:
            break
        ans.append(a_mat_k[i][j])
for i in range(N-1):
    if not (ans[i] <= ans[i+1]):
        print("No")
        exit()

print("Yes")

