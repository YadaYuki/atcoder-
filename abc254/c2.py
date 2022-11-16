N,K = map(int,input().split())
a = list(map(int,input().split()))

k_splited_arr = [[] for _ in range(K)]

for i in range(N):
    k_splited_arr[i%K].append(a[i])

for i in range(K):
    k_splited_arr[i] = sorted(k_splited_arr[i])

ans = []

for i in range(N):
    ans.append(k_splited_arr[i%K][i//K])

ok = ans==sorted(a)
if ok:
    print("Yes")    
else:
    print("No")



