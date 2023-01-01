N = int(input())
A,B,C,D = 1,N,1,N

# ルークが存在しない行を求める
ok,ng = 1,N+1
while ok != ng:
    mid = (ok + ng) // 2
    A,B = ok,mid
    print(f"? {A} {B} {C} {D}")
    T = int(input())
    if (B - A + 1) == T:
        ok = mid + 1
    else:
        ng = mid

X = ok

# ルークが存在しない列を求める
A,B,C,D = 1,N,1,N
ok,ng = 1,N+1
while ok != ng:
    mid = (ok + ng) // 2
    C,D = ok,mid
    print(f"? {A} {B} {C} {D}")
    T = int(input())
    if (D - C + 1) == T:
        ok = mid + 1
    else:
        ng = mid

Y = ok

print(f'! {X} {Y}')


