from bisect import bisect_left
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


Q_idx = [-1] * (N+1) # Q_idx[i] = 配列Q内でiが格納されているindex


for i in range(N):
    Q_idx[Q[i]] = i


idx_ls = [10**9] * N

for i in range(N):
    P_multiple_idx_in_Q = []
    for j in range(P[i],N+1,P[i]):
        P_multiple_idx_in_Q.append(Q_idx[j])
    # print(P_multiple_idx_in_Q)
    P_multiple_idx_in_Q.sort()
    P_multiple_idx_in_Q.reverse()

    for j in P_multiple_idx_in_Q:
        idx_ls[bisect_left(idx_ls,j)] = j
#         print(bisect_left(idx_ls,j),idx_ls)
# print(idx_ls)

print(bisect_left(idx_ls,10**9))
