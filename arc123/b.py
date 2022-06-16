N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

A_used = [[a,False] for a in A]
B_used = [[b,False] for b in B]
C_used = [[c,False] for c in C]
ans = 0
for i in range(N):
    a = A[i]
    # a < B[j] かつ B[j][1] = Falseなjを2部探索で見つける
    ok,ng = N,-1
    while ok - ng > 1:
        mid = (ok+ng) // 2
        b,used = B_used[mid]
        if b > a and (not used):
            ok = mid
        else:
            ng = mid
    if ok == N: # 存在しない
        continue
    
    j = ok
    b = B[j]
    
    # b < C[k] かつ C[k][1] = Falseなkを2部探索で見つける
    ok,ng = N,-1
    while ok - ng > 1:
        mid = (ok+ng) // 2
        c,used = C_used[mid]
        if c > b and (not used):
            ok = mid
        else:
            ng = mid
    
    if ok == N:
        continue
    
    k = ok
    c = C[k]

    B_used[j][1],C_used[k][1] = True,True
    ans += 1


print(ans)