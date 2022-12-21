N = int(input())
l,r = 1,N+1
# ルークが置かれていない列を2部探索で求める

while r - l > 0:
    mid = (r+l) // 2
    A,B,C,D = 1,N,l,mid
    print(f'? {A} {B} {C} {D}')
    T = int(input())
    if T == (mid - l + 1): # ルークが置かれていない列は聞いた範囲ではない範囲に存在する
        l = mid+1
    else:
        r = mid

t,d = 1,N+1
while d - t > 0:
    mid = (t+d) // 2
    A,B,C,D = t,mid,1,N
    print(f'? {A} {B} {C} {D}')
    T = int(input())
    if T == (mid-t + 1): # ルークが置かれていない列は聞いた範囲ではない範囲に存在する
        t = mid + 1
    else:
        d = mid

print(f"! {t} {l}")


