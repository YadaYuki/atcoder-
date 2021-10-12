A,B,X = map(int,input().split())

ok,ng = 0,10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    d = len(str(mid))
    price = A * mid + B * d

    if X >= price: # 価格よりも、所持金の方が多い時。
        ok = mid
    else:
        ng = mid
    
print(ok)

