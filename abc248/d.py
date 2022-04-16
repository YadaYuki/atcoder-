N = int(input())
A = list(map(int, input().split()))
Q = int(input())

idx_dict = {} # {Aの要素: [Aの要素が出現するインデックスのリスト]}

for i, a in enumerate(A):
    if a not in idx_dict:
        idx_dict[a] = [i]
    else:
        idx_dict[a].append(i)


for i in range(Q):
    L,R,X = map(int, input().split())
    if X not in idx_dict:
        print(0)
        continue
    else:
        L-=1
        R-=1
        # L以上の最小値,R以下の最大値を2部探索で求める
        # L以上の最小値
        idx_arr = idx_dict[X]
        ok,ng = len(idx_arr),-1
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if idx_arr[mid] >= L:
                ok = mid
            else:
                ng = mid
        l = ok
        # R以下の最大値
        ok,ng = -1,len(idx_arr)
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if idx_arr[mid] <= R:
                ok = mid
            else:
                ng = mid
        r = ok
        # print(idx_dict)
        print(r-l+1)


        # R以下の最大値

