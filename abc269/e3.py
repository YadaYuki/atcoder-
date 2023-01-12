N = int(input())

# 縦方向
ok,ng = 1,N+1
while (ng - ok) > 0:
    mid = (ok + ng) // 2
    A,B,C,D = ok,mid,1,N
    print(f'? {A} {B} {C} {D}')
    T = int(input())
    if (mid - ok + 1) == T:
        ok = mid + 1
    else:
        ng = mid

X = ok

# 横方向
ok,ng = 1,N+1
while (ng - ok) > 0:
    mid = (ok + ng) // 2
    A,B,C,D = 1,N,ok,mid
    print(f'? {A} {B} {C} {D}')
    T = int(input())
    if (mid - ok + 1) == T:
        ok = mid + 1
    else:
        ng = mid

Y = ok

print(f"! {X} {Y}")
