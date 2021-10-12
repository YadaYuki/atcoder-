R,B = map(int,input().split())
x,y = map(int,input().split())

def check(X): # X個の花束を作ることができるかどうか。
    # 少なくとも各花束一本ずつは必要
    r = R-X
    b = B-X
    if r < 0 or b < 0:
        return False
    # 
    num = r // (x-1) + b // (y-1)
    return num >= X

ok,ng = 0,10**18+1

while abs(ok-ng) > 1:
    mid = (ok+ng)//2

    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)


