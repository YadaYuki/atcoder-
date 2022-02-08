from bisect import bisect_left
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
Q_val_to_idx_arr = [0] * (N+1)

for i in range(N):
    Q_val_to_idx_arr[Q[i]] = i

z = [10**9] * (N)
for a in P:
    multiple_idx_in_Q = []
    for i in range(a,N+1,a):
        multiple_idx_in_Q.append(Q_val_to_idx_arr[i])
    
    multiple_idx_in_Q.sort(reverse=True)

    for idx in multiple_idx_in_Q:
        insert_idx_to_z = bisect_left(z, idx)

        z[insert_idx_to_z] = idx

print(bisect_left(z, 10**9))






