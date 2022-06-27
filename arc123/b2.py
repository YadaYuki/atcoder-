N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
B_used = [[a,False] for a in B]
C_used = [[a,False] for a in C]
ans = 0
for a in A:
    # a < b を満たすようなBの要素bを求める
    ng,ok = -1,N
    while ok - ng > 1:
        mid = (ok + ng) // 2
        b,used = B_used[mid]
        if a < b and (not used):
            ok = mid
        else:
            ng = mid
    
    if ok == N:
        continue

    b,_ = B_used[ok]
    B_used[ok][1] = True

    # b < c を満たすようなCの要素cを求める
    
    ng,ok = -1,N
    
    while ok - ng > 1:
        mid = (ok + ng) // 2
        c,used = C_used[mid]
        if b < c and (not used):
            ok = mid
        else:
            ng = mid
    
    if ok == N:
        continue
    c,_ = C_used[ok]
    C_used[ok][1] = True


    
    ans += 1

print(ans)