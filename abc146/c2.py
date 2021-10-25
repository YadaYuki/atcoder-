A,B,X = map(int,input().split())

ng = 10 ** 9 + 1
ok = 0

while abs(ok-ng) > 1:
    N = (ok + ng) // 2
    price = A * N + B * len(str(N))
    if price <= X:
        ok = N
    else:
        ng = N

print(ok)


