N,K,Q = map(int,input().split())

A = list(map(int,input().split()))
L = list(map(int,input().split()))

for i in range(Q):
    a_idx = L[i]-1
    if A[a_idx] >= N:
        continue
    # 隣のマスに駒があるかどうかをチェック
    if a_idx == K-1:
        A[a_idx] += 1
        continue
    if A[a_idx] + 1 != A[a_idx+1]:
        A[a_idx] += 1
        continue


print(*A)
