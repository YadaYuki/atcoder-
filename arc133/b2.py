from bisect import bisect_left

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

Q_idx = [-1] * (N+1) # Q_idx[i] = 配列Q内でiが格納されているindex

for i in range(N):
    Q_idx[Q[i]] = i


z = [10**9] * N # これのやくわりが分かってない
for i in range(N):
    Q_item_idx_ls = [] # P[i]の倍数が格納されているQのindex
    for j in range(P[i],N+1,P[i]): # jはP[i]の倍数
        Q_item_idx_ls.append(Q_idx[j])

    Q_item_idx_ls.sort()
    Q_item_idx_ls.reverse()

    for j in Q_item_idx_ls:
        z[bisect_left(z,j)]=j






print(bisect_left(z,10**9)) 
# print(z)