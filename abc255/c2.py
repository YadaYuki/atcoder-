X,A,D,N = map(int,input().split())
S_start = A
S_final = A + D * (N-1)
S_min = min(S_start,S_final)
S_max = max(S_start,S_final)

if X <= S_min:
    print(S_min - X)
    exit()
if S_max <= X:
    print(X - S_max)
    exit()

xr_i = (X - A) // D + 1
xl_i = xr_i + 1

xr = A + D * (xr_i - 1)
xl = A + D * (xl_i - 1)

ans = min(abs(X-xr),abs(X-xl))

print(ans)

